# Project 3

Web Programming with Python and JavaScript

NOTE!!! Once an item on the menu is added to the cart, please wait for the page to reload so that it is added properly.

Credentials:
Normal User:
username: jaisharma
password: legodude

Super User:
username: web50
password: legodude

Hello! Welcome to my fourth project for the web programming course. This document is going to give a short overview of what each file does,
and how the program works together. I heavily relied on documentation, help from tutoring, and my tf, David Nunez to get through some of the problems.
Everything within the milestones was completed. The only, very very tiny problem in this code is that the signup page does not format correctly.
As previously stated, I used many sources so I will list just a few below. Furthermore, the rest of the document will focus on the views.py
https://stackoverflow.com/questions/618557/django-using-select-multiple-and-post
https://stackoverflow.com/questions/38675271/django-template-for-loop-inside-select-renders-values-after-the-select?rq=1
https://getbootstrap.com/docs/4.0/components/buttons/
https://docs.djangoproject.com/en/2.0/ref/models/fields/#django.db.models.ForeignKey.on_delete
https://stackoverflow.com/questions/8389880/django-select-option-in-template
https://www.w3schools.com/tags/att_input_value.asp
https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Admin_site
https://getbootstrap.com/docs/4.0/components/buttons/
https://getbootstrap.com/docs/4.0/components/alerts/
https://getbootstrap.com/docs/4.0/components/input-group/
https://stackoverflow.com/questions/625047/django-newbie-reverse-not-found
https://stackoverflow.com/questions/2984987/model-not-showing-up-in-django-admin
https://docs.djangoproject.com/en/2.0/intro/tutorial02/
https://stackoverflow.com/questions/16788380/import-all-classes-or-functions-in-all-files-in-folder-as-if-they-were-all-in
https://simpleisbetterthancomplex.com/tips/2016/07/25/django-tip-8-blank-or-null.html
https://getbootstrap.com/docs/4.0/content/tables/
https://stackoverflow.com/questions/38390177/what-is-a-noreversematch-error-and-how-do-i-fix-it
https://docs.djangoproject.com/en/dev/topics/http/urls/#naming-url-patterns
https://stackoverflow.com/questions/21240680/django-noreversematch
https://stackoverflow.com/questions/21240680/django-noreversematch
https://docs.djangoproject.com/en/2.0/ref/urls/#path
https://stackoverflow.com/questions/16906515/how-can-i-get-the-username-of-the-logged-in-user-in-django
https://docs.djangoproject.com/en/dev/ref/models/instances/#what-happens-when-you-save
https://www.fullstackpython.com/object-relational-mappers-orms.html
https://stackoverflow.com/questions/6305061/get-an-object-attribute
https://docs.djangoproject.com/en/2.0/ref/forms/fields/
https://stackoverflow.com/questions/8609192/differentiate-null-true-blank-true-in-django
https://getbootstrap.com/docs/4.0/components/forms/
https://simpleisbetterthancomplex.com/tutorial/2018/01/29/how-to-implement-dependent-or-chained-dropdown-list-with-django.html
https://stackoverflow.com/questions/1107737/numeric-for-loop-in-django-templates
https://www.pythoncentral.io/pythons-range-function-explained/
https://docs.djangoproject.com/en/dev/ref/templates/builtins/?from=olddocs#for
https://stackoverflow.com/questions/5653533/indexerror-list-assignment-index-out-of-range
https://stackoverflow.com/questions/1107737/numeric-for-loop-in-django-templates
https://stackoverflow.com/questions/31015333/django-pass-a-select-form-post-data-from-one-view-to-another
https://stackoverflow.com/questions/618557/django-using-select-multiple-and-post
https://stackoverflow.com/questions/618557/django-using-select-multiple-and-post
https://stackoverflow.com/questions/11586038/how-to-get-the-value-from-the-drop-down-box-django
https://stackoverflow.com/questions/10065676/django-hide-button-in-template-if-user-is-not-super-user
https://www.quora.com/How-can-you-limit-a-Django-view-to-a-super-user-only-and-if-the-user-is-not-a-super-user-display-an-error-page

Whew

Views.py:

index:
The index loads the menu for the user to purchase food. It is not the main route, and is only accessible through login.

signup:
This function adds a user to the users table and signs them up for the website. It retrieves the infomraiton from the HTML page.

login_view:
Logs the user in if they have been authenticated with the table.

logout_view:
Logs the user out using Django functions

login_r:
Simply a redirect

carted:
Adds the users items to the cart and is only accessible if the user is logged in using the login decorator. It simply adds the users order
to the correct table so that it can be displayed later. NOTE!!! Once an item on the menu is added to the cart, please wait for the page
to reload so that it is added properly.

view_cart:
Displays the cart, and passes back the users' order from the correct table. Also allows them to add toppings within the html file.

confirm_order:
Confirms the users order and adds it to the confirmed order table so that the admin can visit it as needed. This function aslo retrieves
the select data and adds it to the Toppings charfield.

order_admin:
This is an admin page to see all of the orders. It is only accessible by a superuser and they see a button above view cart when they are logged in.

remove_admin:
Deletes an order admin side

remove_user:
Deletes an order user side

urls.py:
These are the urls that route to different paths and functions within the views.py file.

Thanks for grading! Have a good day.