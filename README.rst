============
django-scian
============

django-scian is a Django app to get a SCIAN Catalog.


Quick start
-----------

1. Add "polls" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...,
        "django_scian.apps.ScianConfig",
    ]

2. Include the polls URLconf in your project urls.py like this::

    path("scian/", include("django_scian.urls")),

3. Run ``python manage.py migrate`` to create the models.

4. Start the development server and visit the admin to see the tree.

5. Visit the ``/scian/`` URL to participate in the poll.
