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


How to manage the invitation codes with the admin panel?
--------------------------------------------------------

1. Open up your admin.py

2. Paste the following code inside, (remember to structure keep the structure):

	from .models import InvitationCode
	
	class InvitationCodeAdmin(admin.ModelAdmin):
	    list_display = ( 'code', 'user', 'is_used', 'used_date', 'issued_date')
	    list_filter = ( 'user', 'issued_date',)
	    readonly_fields=('code',)
	    
	    # Prevent anyone from adding Invitation Codes without the hashing script.
	    def has_add_permission(self, request):
	        return False


    admin.site.register(InvitationCode, InvitationCodeAdmin)

3. Ready! Now you can keep track of all the used codes, and know when to generate more.


How to implement the codes with my registration view inside views.py
--------------------------------------------------------------------

TODO