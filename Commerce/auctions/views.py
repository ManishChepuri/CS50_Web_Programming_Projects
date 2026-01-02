from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.text import slugify
from .models import User, AuctionListing, Bid, WatchlistItem, Comment


def index(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        starting_bid = request.POST["starting_bid"]
        image_url = request.POST.get("image_url")
        category = request.POST.get("category")

        AuctionListing.objects.create(
                seller=request.user,
                title=title,
                slug=slugify(title),
                description=description, starting_bid=starting_bid,
                image_url=image_url,
                category=category)

    return render(request, "auctions/index.html", {
        "name": "Active Listings",
        "active_listings": AuctionListing.objects.all()
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def new_listing(request):
    return render(request, "auctions/new_listing.html", {
        "categories": [category[0] for category in AuctionListing.CATEGORIES]
    })

def listing(request, slug):
    error = ""
    listing = AuctionListing.objects.get(slug=slug)
    if request.method == "POST":
        if request.POST["type"] == "bid":
            bid_price = float(request.POST["new_bid"])
            all_bids = Bid.objects.filter(item=listing).order_by("-bid_price")
            starting_bid = float(listing.starting_bid)
            curr_price = None if not all_bids.first() else float(all_bids.first().bid_price)
            if all_bids.count() == 0 and bid_price < starting_bid:
                    error = "Your Bid Must be at least as Large as the Starting Bid"

            elif curr_price and bid_price <= curr_price:
                error = "Your Bid Must be Larger the than Current Bid"

            else:
                Bid.objects.create(
                    bidder=request.user,
                    item=listing,
                    bid_price=bid_price
                )
        elif request.POST["type"] == "listing_status":
            listing.active=False
            listing.save()
        elif request.POST["type"] == "new_comment":
            Comment.objects.create(
                user=request.user,
                listing=listing,
                content=request.POST["comment"]
            )

    listing = AuctionListing.objects.get(slug=slug)
    highest_bid = Bid.objects.filter(item=listing).order_by("-bid_price").first()
    num_bids = Bid.objects.filter(item=listing).count()
    in_watchlist = WatchlistItem.objects.filter(user=request.user, listing=listing).exists()
    comments = Comment.objects.filter(listing=listing).order_by("-datetime")

    return render(request, "auctions/listing.html", {
        "listing": listing,
        "highest_bid": highest_bid,
        "num_bids": num_bids,
        "in_watchlist": in_watchlist,
        "error": error,
        "comments": comments
    })

def watchlist(request, username):
    if request.method == "POST":
        listing_id = request.POST["listing_id"]
        listing = AuctionListing.objects.get(id=listing_id)
        user = User.objects.get(username=username)
        if request.POST["action"] == "add":
            WatchlistItem.objects.create(
                user=user,
                listing=listing
            )
        else:
            item = WatchlistItem.objects.get(
                user=user,
                listing=listing
            )
            item.delete()
        return redirect("listing", slug=listing.slug)

    else:
        user = User.objects.get(username=username)
        qs = WatchlistItem.objects.filter(user=user)
        ids = qs.values_list('listing', flat=True)
        watchlist_listings = AuctionListing.objects.filter(id__in=ids)
        return render(request, "auctions/watchlist.html", {
            "watchlist_listings": watchlist_listings
        })

def categories(request):
    categories = [category[0] for category in AuctionListing.CATEGORIES]
    return render(request, "auctions/categories.html", {
        "categories": categories
    })

def category(request, category):
    return render(request, "auctions/index.html", {
        "name": "Category: " + category,
        "active_listings": AuctionListing.objects.filter(category=category)
    })
