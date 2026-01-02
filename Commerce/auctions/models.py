from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    def __str__(self):
        return f"{self.username}"

class AuctionListing(models.Model):
    CATEGORIES = [
        ('Electronics', 'Electronics'),
        ('Fashion', 'Fashion'),
        ('Books', 'Books'),
        ('Home', 'Home'),
    ]


    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_listings")
    title = models.CharField(max_length=128)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    starting_bid = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=50, choices=CATEGORIES, blank=True, null=True)
    datetime = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} | {self.seller} | {self.starting_bid} | {self.datetime}"

class Bid(models.Model):
    bidder = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_bids")
    item = models.ForeignKey(AuctionListing, on_delete=models.CASCADE, related_name="item_bids")
    bid_price = models.DecimalField(max_digits=10, decimal_places=2)
    datetime = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.bidder} | {self.item} | {self.bid_price} | {self.datetime}"

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_comments")
    listing = models.ForeignKey(AuctionListing, on_delete=models.CASCADE, related_name="listing_comments")
    content = models.TextField()
    datetime = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}: {self.content}  -  {self.date_published}"

class WatchlistItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_watchlist_items")
    listing = models.ForeignKey(AuctionListing, on_delete=models.CASCADE, related_name="auctionlisting_watchlist_items")
    datetime = models.DateField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'listing'], name="unique_user_listing")
        ]
