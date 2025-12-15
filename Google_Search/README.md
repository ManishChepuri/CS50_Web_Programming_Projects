# CS50 Web Programming: Google Search Front-End

This project implements a front-end for **Google Search**, **Google Image Search**, and **Google Advanced Search** as part of CS50’s Web Programming course. The goal was to replicate key functionality of Google’s search interface using HTML and CSS.

## Features

### Google Search (`index.html`)
- “Google Search” button that redirects to Google search results for the entered query.
- “I’m Feeling Lucky” button that redirects directly to the top result.
- Links in the top-right corner to **Image Search** and **Advanced Search** pages.

### Google Image Search (`images.html`)
- Search input field for image queries.
- Redirects to Google Images search results for the entered query.
- Link back to main Google Search page.

### Google Advanced Search (`advanced.html`)
- Four input fields to filter searches:
  - All these words
  - This exact word or phrase
  - Any of these words
  - None of these words
- Redirects to Google search results for the given query.
- Link back to main Google Search page.

## Implementation Details
- All forms submit via **GET** to Google’s search endpoints.
- The `q` parameter is used for queries; additional parameters for advanced search are included in hidden input fields where necessary.
- CSS is styled to resemble Google’s aesthetics.

## Getting Started
1. Open `index.html`, `images.html`, or `advanced.html` in a browser.
2. Type a query and click the relevant search button.
3. You will be redirected to Google search results.