# CS50W Mail Project

## Overview

This is a single-page email client built using **JavaScript, HTML, CSS, and Django**. The application allows users to send, receive, archive, and reply to emails. All emails are stored in a Django database; no real email servers are used. The front-end is a single-page application where JavaScript controls the interface and API calls handle email operations.

---

## Features

1. **Send Mail**
   - Users can compose and send emails.
   - Composing an email requires recipients, subject, and body.
   - Emails are sent via a POST request to `/emails`.
   - Upon successful sending, the Sent mailbox is loaded.

2. **Mailbox View**
   - Supports **Inbox**, **Sent**, and **Archived** mailboxes.
   - Mailboxes are loaded dynamically with a GET request to `/emails/<mailbox>`.
   - Emails are displayed in a vertical list with:
     - Sender
     - Subject
     - Timestamp
     - Background color indicating read/unread status.

3. **View Email**
   - Clicking an email displays its content.
   - Shows sender, recipients, subject, timestamp, and body.
   - Marks the email as read automatically via a PUT request.

4. **Archive / Unarchive**
   - Users can archive or unarchive emails using a button in the email view.
   - Changes are sent via a PUT request to `/emails/<email_id>`.
   - Archived emails are removed from the Inbox and moved to the Archive mailbox.

5. **Reply**
   - Users can reply to emails.
   - Opens the compose view prefilled with:
     - Recipient: original sender
     - Subject: prefixed with `Re:` if not already
     - Body: includes the original message and timestamp

---

## Technologies Used

- **Front-end**: HTML, CSS, JavaScript (Single Page Application)
- **Back-end**: Django
  - Models for Email
  - API endpoints to send, retrieve, and update emails
- **Database**: SQLite

---

## API Endpoints

1. **GET /emails/<mailbox>**
   - Returns a list of emails in the specified mailbox (`inbox`, `sent`, or `archive`).
   - Example JSON response:
   ```json
    {
        "id": 100,
        "sender": "foo@example.com",
        "recipients": ["bar@example.com"],
        "subject": "Hello!",
        "body": "Hello, world!",
        "timestamp": "Jan 2 2020, 12:00 AM",
        "read": false,
        "archived": false
    }
    ```
2. **GET /emails/<email_id>**
    - Returns the details of a single email.
    - Example JSON response:
    ```json
    {
        "id": 100,
        "sender": "foo@example.com",
        "recipients": ["bar@example.com"],
        "subject": "Hello!",
        "body": "Hello, world!",
        "timestamp": "Jan 2 2020, 12:00 AM",
        "read": false,
        "archived": false
    }
    ```
3. **POST /emails**
    - Sends a new email.
    - Requires JSON body:
    ```json
    {
        "recipients": "baz@example.com",
        "subject": "Meeting time",
        "body": "How about we meet tomorrow at 3pm?"
    }
    ```
4. **PUT /emails/<email_id>**
    - Updates email properties (read/unread or archived/unarchived).
    - Example body to mark as read:
    ```json
    { "read": true }
    ```
    - Example body to archive:
    ```json
    { "archived": true }
    ```

---

## Installation & Setup

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





