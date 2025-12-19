# CS50 Web Programming: Wiki Project

## Overview

This project is a Wikipedia-like online encyclopedia built using **Django** and **Markdown**. Users can view, create, edit, and search encyclopedia entries. Each entry is stored as a Markdown file and rendered into HTML for display.


## Features

1. **Entry Pages**

   * Visit `/wiki/TITLE` to view an encyclopedia entry.
   * If an entry does not exist, an error page is shown.
   * Markdown content is converted to HTML for display.

2. **Index Page**

   * Lists all encyclopedia entries.
   * Users can click on an entry name to visit its page.

3. **Search**

   * Exact matches redirect to the corresponding entry page.
   * Partial matches show a list of all entries containing the search query.

4. **Create New Page**

   * Users can create new encyclopedia entries.
   * Entry titles must be unique; duplicate titles result in an error.
   * New entries are saved as Markdown files.

5. **Edit Page**

   * Existing entries can be edited.
   * The edit page pre-populates with the current Markdown content.
   * Changes are saved and displayed on the updated entry page.

6. **Random Page**

   * Clicking “Random Page” redirects the user to a random encyclopedia entry.


## Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone https://github.com/ManishChepuri/CS50_Web_Programming_Projects.git
   cd wiki
   ```

2. **Install dependencies:**

   ```bash
   pip3 install django markdown2
   ```

3. **Run the development server:**

   ```bash
   python3 manage.py runserver
   ```

4. **Open in browser:**

   ```
   http://127.0.0.1:8000/
   ```


## Usage

* Navigate to the homepage to view all entries.
* Use the search bar to find specific entries.
* Click “Create New Page” to add an entry.
* Use the “Edit” link on any entry page to modify it.
* Click “Random Page” to explore a random article.