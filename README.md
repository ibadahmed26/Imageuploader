# Imageuploader

This is a mini Authenticated web application based on Django (MTV) and HTML.

based on Signup and Login forms that uses session backend of Django(default auth) to Authenticate members into application.

Application is basically a image uploader where registered users can upload wallpaper/images.

Simple I worked on MEDIA_URL, MEDIA_ROOT, HTML rendering, Django Auth forms, Static directory and Login&Logout functions and techniques.

WORKING:

-User can register into database

-User can login through simple Authentication (Django session auth - default)

-Dashboard appear where ImageField is waiting to take img input from registered users only

-If user is not authenticated OR Anonymous , He/She can't upload image on webapp

-Image will save in database through Pillow package in external storage (MEDIA_ROOT)

-if user want to upload image authentication required otherwise he/she will only can view images and incase of uploading image redirect to login page.

-No user can views loginpage again once user already authenticated (extra point to safe re-login)

-Simply at last user can logout
