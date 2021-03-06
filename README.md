# homepage-django

> __This setup has been retired__

This is the open-source repository for my Django-based homepage. Key elements of the website are:

 - Page content management through admin panel
 - Page contents written in Markdown
 - Minimal responsive styling

## Default Outline

The website is first of all developed in mobile first sense. Thus it is fully responsive, which is explicitly visible with the navigation elements. With viewport sizes smaller than phablet, the links to pages are accessible through a clickable icon. With greater sizes, the links are straight-up visible.

Under the hood the website is a full-fledged Django project, with distinct pages and the header for example rendered on-the-fly from persisted Django models. The page contents are written in Markdown, which are then automatically rendered to HTML elements. The website has been built to enable the editing of existing page contents without the need to touch the source codes. This is all done through the admin panel.

In case of needing a new page however, a URL-route has to be set up to match the slug (i.e. `main-page`) if the page. The dynamic creation of URL-routes hasn't been implemented, at least not yet.

The page uses modified [SkeletonCSS](www.getskeleton.com) for responsive styles and [Font Awesome 4](http://fontawesome.io/) for icons.

## Setting Up the Project

Here are the necessary steps to get the project up and running. Please notice that more in-depth Raspberry Pi tutorial is given in the ``/deployment/RASPBERRY.md`` to which you can refer for server configuration.

### Install Packages

Required packages are listed below. 

    django
    requests
    django-markdownx

However you must define your Python version accordingly and test that the website application runs fine with it.

### Perform Migrations

The SQLite3 database will not be shipped with the project and needs to be initialized before first run. To do this, first prepare the mgirations by navigating to the path `.../homepage-django/app` and calling

    python manage.py makemigrations

and

    python manage.py migrate

directly after that. This will create the default pages titled *Main Page*, *About Me* and *Career Bio*. 

### Create a Superuser

To access the website's admin panel, you must also create a Django super user. This can be achieved by navigating to the path `.../homepage-django/app` and calling

    python manage.py createsuperuser

and following the instructions after. This is required for activating the LinkedIn API in the Admin panel

### Test the Website

After succesfully installing the virtual environment, navigate to the path `.../homepage-django/app` in a terminal. With default virtual environment settings you should then activate the virtual environment by calling either

    source activate django

or
    
    activate django

respective of your OS.

Then call

    python manage.py runserver

and navigate to the host address presented in the terminal.

### Add LinkedIn API

Then navigate to the ``/admin`` page and add a new LinkedIn API Client. Required information is found in the respective LinkedIn Developer app registered for the webpage. Two crucial endpoints to use in creating the client are:

    http://host/linkedin-auth
    http://host/linkedin-callback

The latter has to be also registered as viable callback URL in the LinkedIn API app.
