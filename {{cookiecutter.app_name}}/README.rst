===============================
{{ cookiecutter.project_name }}
===============================

{{ cookiecutter.project_short_description}}


Quickstart
----------

First, set your app's secret key as an environment variable. For example, example add the following to ``.bashrc`` or ``.bash_profile``.

.. code-block:: bash

    export {{cookiecutter.app_name | upper}}_SECRET='something-really-secret'


Then run the following commands to bootstrap your environment.


::

    git clone https://github.com/{{cookiecutter.github_username}}/{{ cookiecutter.app_name }}
    cd {{cookiecutter.app_name}}
    pip install -r requirements/dev.txt
    python manage.py server

You will see a pretty welcome screen.

Once you have installed your DBMS, run the following to create your app's database tables and perform the initial migration:

::

    python manage.py db init
    python manage.py db migrate
    python manage.py db upgrade
    python manage.py server



Bluemix Deployment
-------------------

In your production environment, make sure the ``{{cookiecutter.app_name|upper}}_ENV`` environment variable is set to ``"prod"`` through the manifest.yml file. You can also set the secret key for your production environment there (don't commit the yaml file GitHub in that case).


Vendor in all your requirements by running inside your project folder:

::

    # vendors all the pip *.tar.gz into vendor/
    pip install --download vendor -r requirements.txt

Login to the cf commandline environment for your region (in the example we use UK)::

    cf login -a api.eu-gb.bluemix.net

then push the app (memory requirements are already in the yaml file)::

    cf push {{ cookiecutter.project_name }}

Shell
-----

To open the interactive shell, run ::

    python manage.py shell

By default, you will have access to ``app``, ``db``, and the ``User`` model.


Running Tests
-------------

To run all tests, run ::

    python manage.py test


Migrations
----------

Whenever a database migration needs to be made. Run the following commands:
::

    python manage.py db migrate

This will generate a new migration script. Then run:
::

    python manage.py db upgrade

To apply the migration.

For a full migration command reference, run ``python manage.py db --help``.
