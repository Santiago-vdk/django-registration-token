=========================
django-registration-token
=========================

.. image:: https://travis-ci.org/Santiago-vdk/django-registration-token.svg?branch=master
    :target: https://travis-ci.org/Santiago-vdk/django-registration-token

A Django 1.8+ auth backend that implements user generated tokens to register users.

django-registration-token is a simple system that prevents unwanted
users from accessing the content, it implements a script that
adds several random generated tokens to the database and manages
when a token is issued and used.


Quick start
-----------

1. Add "django-registration-token" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'django-registration-token',
    ]

2. Run `python manage.py migrate` to create the InvitationCode model.

3. Run the following command to generate any ammount of token models.

	
	>> python manage.py gen-invitation-codes "ammount"
	...


	*Generation algorithm explained later.

	

4. Implement the token validation on your registration view inside views.py.

	YES, I will add an example for point "4".