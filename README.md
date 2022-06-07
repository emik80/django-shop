# django-shop

_Simple education project for e-shop on Python 3.10 + Django 3 + SQLite db._

#### What do we have?

1. Registration.
2. Authentication.
3. Item's catalog with categories.
4. Cart.
5. Personal client account with orders history.
6. Pay gates based on fondy.eu.
7. Django admin-panel for easy goods and orders management.

#### For correct usage you must do the following:

1. Input your email settings (I did it for Gmail, but you can choose your option) for the contact form in the file /eshop/mysite/mysite/post_settings.py
   * EMAIL_HOST_USER = 'youremail'
   * EMAIL_HOST_PASSWORD = 'yourpassword'
   * RECIPIENT_LIST = ['youremail1', 'youremail2', ] 
2. In /eshop/mysite/mysite/shop/templates/shop/account.html (string #40) insert yor domain url for correct fondy callback


_* Hmart – Electronics eCommerce HTML Template is used (for educational purposes< not for commerce use!!!)_