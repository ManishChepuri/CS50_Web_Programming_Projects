# Commerce – CS50W Project 2

An eBay-like e-commerce auction site built with Django, allowing users to create auction listings, place bids, comment on listings, and manage a personal watchlist.

This project is part of **CS50’s Web Programming with Python and JavaScript** and fulfills all requirements outlined in Project 2: *Commerce*.

---

## 🚀 Features

### 🔐 Authentication
- User registration, login, and logout
- Conditional UI rendering based on authentication status

### 📦 Auction Listings
- Create new auction listings with:
  - Title
  - Description
  - Starting bid
  - Optional image URL
  - Optional category
- View all **active listings** on the homepage
- Close auctions (only by the listing creator)

### 💰 Bidding System
- Users can place bids on active listings
- Bids must:
  - Be **greater than or equal to the starting bid**
  - Be **greater than the current highest bid**
- Error messages shown for invalid bids
- Highest bidder becomes the winner when an auction is closed

### 💬 Comments
- Signed-in users can comment on listings
- All comments are displayed on the listing page

### ⭐ Watchlist
- Users can add or remove listings from their watchlist
- Personalized watchlist page showing saved listings

### 🗂 Categories
- Listings can be assigned to categories
- Category pages display all active listings in that category

### 🛠 Admin Interface
- Django admin panel allows administrators to:
  - View, create, edit, and delete listings
  - Manage bids
  - Manage comments

---

## 🧱 Models

The application includes the following models:

- **User**
  - Inherits from `AbstractUser`
- **Listing**
  - Title
  - Description
  - Starting bid
  - Image URL (optional)
  - Category (optional)
  - Creator
  - Active status
- **Bid**
  - Bid amount
  - Bidder
  - Associated listing
- **Comment**
  - Comment text
  - Author
  - Associated listing

Additional relationships include:
- A many-to-many relationship between users and listings for the **watchlist**

---

## 🖥 Pages Overview

| Page | Description |
|----|----|
| `/` | Active listings homepage |
| `/login` | User login |
| `/register` | User registration |
| `/listing/<id>` | Individual listing page |
| `/create` | Create a new listing |
| `/watchlist` | User watchlist |
| `/categories` | List of all categories |
| `/categories/<category>` | Listings filtered by category |
| `/admin` | Django admin panel |

---

## ⚙️ Installation & Setup

### 1. Download Distribution Code
Download and unzip the project distribution:

### 2. Navigate to the Project Directory
```bash
cd commerce
```
### 3. Apply Migrations
```bash
python manage.py makemigrations auctions
python manage.py migrate
```
### 4. Run the Development Server
```bash
python manage.py runserver
```

