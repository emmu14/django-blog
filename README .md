# Django Blog & Shop

A Django web app where users can sign up, publish articles with images, and buy items through a shopping cart with a checkout flow.

## Features

- User registration, login, and logout
- Create, view, and read articles (with detail pages)
- Image uploads for articles
- Shopping cart: add, remove, and view items
- Checkout and payment-success page
- Responsive layout with CSS

## Tech Stack

Python · Django · HTML · CSS · Django ORM (SQLite) · Git/GitHub

## Screenshots

| | |
|---|---|
| ![Screenshot 1](Screenshot%202026-10-22%20150116.png) | ![Screenshot 2](Screenshot%202026-10-22%20150324.png) |
| ![Screenshot 3](Screenshot%202026-10-22%20150343.png) | ![Screenshot 4](Screenshot%202026-10-22%20150412.png) |

## Project Structure

```
├── accounts/       # Login, signup, authentication
├── articles/       # Articles, images, cart, checkout
├── templates/      # HTML templates
├── assets/css/     # Stylesheets
├── media/images/   # Uploaded images
├── db.sqlite3      # Local SQLite database
└── manage.py
```

## Getting Started

```bash
# 1. Clone
git clone https://github.com/emmu14/django-blog.git
cd django-blog

# 2. Virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install django pillow       # or: pip install -r requirements.txt

# 4. Set up the database
python manage.py migrate

# 5. Create an admin user (optional)
python manage.py createsuperuser

# 6. Run the server
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

## Future Improvements

- [ ] Automated tests
- [ ] Stronger security and form validation
- [ ] Production deployment
- [ ] Real payment gateway (e.g., Stripe or Razorpay)

## Author

**Emmanuvel Christin**
GitHub: [@emmu14](https://github.com/emmu14) · LinkedIn: <your-link>
