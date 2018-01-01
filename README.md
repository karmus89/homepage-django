# homepage-django

This is the open-source repository for my Django-based homepage. Key elements of the website are:

 - Page content management through admin panel
 - Page contents written in Markdown
 - Minimal responsive styling

## Default outline

The website is first of all developed in mobile first sense. Thus it is fully responsive, which is explicitly visible with the navigation elements. With viewport sizes smaller than phablet, the links to pages are accessible through a clickable icon. With greater sizes, the links are straight-up visible.

Under the hood the website is a full-fledged Django project, with distinct pages and the header for example rendered on-the-fly from persisted Django models. The page contents are written in Markdown, which are then automatically rendered to HTML elements. The website has been built to enable the editing of existing page contents without the need to touch the source codes. This is all done through the admin panel.

In case of needing a new page however, a URL-route has to be set up to match the slug (i.e. `main-page`) if the page. The dynamic creation of URL-routes hasn't been implemented, at least not yet.

The page uses modified [SkeletonCSS](www.getskeleton.com) for responsive styles and [Font Awesome 4](http://fontawesome.io/) for icons.

## Setting up the project

Here are the necessary steps to get the project up and running.

### Create a virtual environment

Here you have two options.

#### Option 1: Create from file

First thing required is setting up the development environment. In the root of the project there is a file named `venv_ubuntu.yml` or `venv_pi.yml` respective of your target OS. The dependency file contains all the required information for setting up the Python virtual environment with `conda`.

First install conda:

    pip install conda

Then navigate to the project root in a terminal and run (for example):

    conda env create -f venv_ubuntu.yml

This should be enough. Otherwise consult [Conda documentation](https://conda.io/docs/) for using files with virtual environment creation and troubleshooting the problems. The `venv_ubuntu.yml` has been created with `conda env export` so there should be no gimmicks implemented by me.

#### Option 2: Install packages by hand

Required packages and their preferred install methods are listed below. 

Preferably with `conda install`:

    django
    requests

With `pip install`:

    django-markdownx

However you must define your Python version accordingly and test that the website application runs fine with it.

### Create a superuser

To access the website's admin panel, you must also create a Django super user. This can be achieved by navigating to the path `.../homepage-django/app` and calling

    python manage.py createsuperuser

and following the instructions after.

### Perform migrations

The SQLite3 database will not be shipped with the project and needs to be initialized before first run. To do this, first prepare the mgirations by navigating to the path `.../homepage-django/app` and calling

    python manage.py makemigrations

and

    python manage.py migrate

directly after that. This will create the default pages titled *Main Page*, *About Me* and *Career Bio*. 

### Start the server

After succesfully installing the virtual environment, navigate to the path `.../homepage-django/app` in a terminal. With default virtual environment settings you should then activate the virtual environment by calling either

    source activate django

or
    
    activate django

respective of your OS.

Then call

    python manage.py runserver

and navigate to the host address presented in the terminal.


