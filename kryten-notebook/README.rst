=====
Kryten Notebook
=====

Kryten Notebook is a simple Django app to display and execute Jupyter notebooks.

Detailed documentation is in the "docs" directory.

Quick start
-----------

0. Install Pypi package

    pip install kryten-logicbook

1. Add application to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'logicbook.apps.LogicbookConfig',
        ...
    ]


2. Include the URLconf in your project urls.py like this::

    url(r'^logicbook/', include('logicbook.urls')),

3. Run `python manage.py migrate` to create the models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/logicbook/ to participate in the IPython console.