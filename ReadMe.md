# Welcome to Django's Starter Project
This is a project from [Django's Documentation Tutorial](https://docs.djangoproject.com/en/2.2/intro/tutorial01/) to get our feet wet in Django framework.

## [Page 1](https://docs.djangoproject.com/en/2.2/intro/tutorial01/) Creating A Project -> Creating An App
### Creating A Project
    ```$ django-admin startproject mysite //where mysite is the name of the project's directory``` 
- These files are:
	•	The outer __mysite/__ root directory is just a container for your project. Its name doesn’t matter to Django; you can rename it to anything you like.
	•	__manage.py__: A command-line utility that lets you interact with this Django project in various ways. You can read all the details about manage.py in django-admin and manage.py.
	•	The inner __mysite/__ directory is the actual Python package for your project. Its name is the Python package name you’ll need to use to import anything inside it (e.g. mysite.urls).
	•	mysite/__init__.py: An empty file that tells Python that this directory should be considered a Python package. If you’re a Python beginner, read more about packages in the official Python docs.
	•	__mysite/settings.py__: Settings/configuration for this Django project. Django settings will tell you all about how settings work.
	•	__mysite/urls.py__: The URL declarations for this Django project; a “table of contents” of your Django-powered site. You can read more about URLs in URL dispatcher.
	•	__mysite/wsgi.py__: An entry-point for WSGI-compatible web servers to serve your project. See How to deploy with WSGI for more details.

- To run and test if our Django project works, go to outer __mysite__ directory and run in terminal:
    ```$ python manage.py runserver```
### Creating An App
- To __create your app__, type this in the same directory as __manage.py__ and run in terminal:
    ```$ python manage.py startapp polls //polls directory and its files will be created```
- To __write a review__:
    ```
    polls/views.py¶
    from django.http import HttpResponse

    def index(request):
        return HttpResponse("Hello, world. You're at the polls index.")
    ```
- To __call the view__, we need to map it to a URL - and for this we need a URLconf. To create a URLconf in the polls directory, create a file called __urls.py__ and type this inside it:
    ```
    polls/urls.py¶
    from django.urls import path
    from . import views

    urlpatterns = [
        path('', views.index, name='index'),
    ]
    ```
- The next step is to __point the root URLconf__ at the polls.urls module in __mysite/urls.py__. Make sure you have an import for __django.urls.include__ and insert an include() in the urlpatterns list like so:
    ```
    mysite/urls.py¶
    from django.contrib import admin
    from django.urls import include, path

    urlpatterns = [
        path('polls/', include('polls.urls')),
        path('admin/', admin.site.urls),
    ]
    ```
- The __include()__ function allows referencing other URLconfs. Whenever Django encounters include(), it chops off whatever part of the URL mattched up to that point and sends the remaining string to the included URLconf for further processing. include() make it easy to plug-and-play URLs. Since polls are in their own URLconf (polls/urls.py), they can be palced under _"/polls/"_, or under _"/fun_polls"_, or under "/content/polls/", or any other path root, and the app will still work
    - __When to use include()__ - You should always use include() when you include other URL patterns. admin.site.urls is the only exception to this.
- To verify that an index view has been wire into the URLconf, run the following command:

    ``` $ python manage.py runserver ```
### path()
- The __path()__ function is passed four arguments, two reuired: __route__ and __view__, and two optionals: __kwargs__, and __name__
    __REQUIRED__
    - __route__ - is a string that contains a URL pattern. When processing a request, Django starts at the first pattern in __urlpatterns__ and makes its way down the list, comparing the requested URL against each pattern until it finds one that matches.
        - Patterns don’t search GET and POST parameters, or the domain name. For example, in a request to https://www.example.com/myapp/, the URLconf will look for myapp/. In a request to https://www.example.com/myapp/?page=3, the URLconf will also look for myapp/
    - __view__ - When Django finds a matching pattern, it calls the specified view function with an __HttpRequest__ object as the first argument and any “captured” values from the route as keyword arguments
    __OPTIONAL__
    - __kwargs__ - _arbitrary keyword arguments_ can be passed in a dictionary to the target view
    - __name__ - _naming your URL lets you refer to it unambiguously from elsewhere_ in Django, especially from within templates. This powerful feature allows you to make global changes to the URL patterns of your project while only touching a single file.

========

## [Page 2](https://docs.djangoproject.com/en/2.2/intro/tutorial02/) Database Setup -> Creating Models
### Database Setup
- __mysite/settings.py__ is a normal Python module with module-level variables representing Django settings, which on default uses SQLite
    - set __TIME_ZONE__ to your time zone
- __INSTALLED_APPS__ holds the names of all Django applications that are activated in this Django instance. Apps can be used in multiple projects, and can be packaged and distributed for use by others in their projects
    - By default, INSTALLED_APPS contains the following apps, all of which come with Django:
        - __django.contrib.admin__ – The admin site. You’ll use it shortly.
        - __django.contrib.auth__ – An authentication system.
        - __django.contrib.contenttypes__ – A framework for content types.
        - __django.contrib.sessions__ – A session framework.
        - __django.contrib.messages__ – A messaging framework.
        - __django.contrib.staticfiles__ – A framework for managing static files.
- ```$ python manage.py migrate``` - command to create the tables in the database in order to use them
    - __migrate__ commands looks at the __INSTALLED_APPS__ setting and creates any necessary database tables according to the database settings in your __mysite/settings.py__ file and teh database migrations shipped with the app
    - __migrate__ command will only run migrations for apps in __INSTALLED_APPS__
### Creating Models
- __Migrations__ are Django's way of communicating changes you make to your models (adding a field, deleting a model, etc.) into your database schema
- A __model__ is the single, definitive source of truth about your data which contains __fields__ and __behaviors__ of the data you're storing. Django follows DRY principle and has the goal to define your data model in one place and automatically derive things from it.
    - checkout /polls/models.py to see an example of model
    - ForeinKey tells Django that each Choice is related to a single Question

