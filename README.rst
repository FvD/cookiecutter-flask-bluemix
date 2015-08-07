cookiecutter-flask-bluemix
===========================

A Flask template for cookiecutter_ that will allow your app to be hosted on `IBM Bluemix`_. It exactly the same as cookiecutter-flask_ by Steven Loria, with the additional manifest.yml and runtime files required by cloudfoundry on Bluemix.

.. _cookiecutter: https://github.com/audreyr/cookiecutter

.. _IBM Bluemix: https://bluemix.net

.. _cookiecutter-flask: https://github.com/sloria/cookiecutter-flask

.. image:: https://travis-ci.org/sloria/cookiecutter-flask.svg
    :target: https://travis-ci.org/sloria/cookiecutter-flask
    :alt: Build Status


Use it now
----------
::

    $ pip install cookiecutter
    $ cookiecutter https://github.com/FvD/cookiecutter-flask-bluemix.git

You will be asked about your basic info (name, project name, app name, etc.). This info will be used in your new project.

Push to Bluemix
---------------
Before you push to bluemix you may want to check (at least) two items:

1. The runtime.txt file specifies python 3.4.3. You can change that to whatever you prefer

2. The settings in the manifest.yml file include the default app name and reserved memory. Please check those and change the settings to your own requirements.

Once you have checked the two files above login to cloudfoundry with the cf-cli you can set up your app and bind an database service. You can also do this through the cf command line with `cf create service <service> <plan>` but the Bluemix interface seems more useful when trying things out. Note that in this example the settings to read the database are for elephantSQL.

Once you have a service bound to your app you can push the app to Bluemix::
    
    $ cf login
    $ cf push  my-app

Features and Screenshots
--------------------------

Please refer to the `original project`_ for features and screenshots. This fork may well be behind the flask aspects, but hopefully useful as a reference for Bluemix deployment.

.. _original project: https://github.com/sloria/cookiecutter-flask

