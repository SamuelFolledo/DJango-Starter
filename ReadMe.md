# Welcome to Django's Starter Project
This is a project from [Django's Documentation Tutorial](https://docs.djangoproject.com/en/2.2/intro/tutorial01/) to get our feet wet in Django framework.

## Page 1
- To create a project, type in terminal
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

===

## Page 2

