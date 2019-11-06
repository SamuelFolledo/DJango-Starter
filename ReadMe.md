# Welcome to Django's Starter Project
This is a project from [Django's Documentation Tutorial](https://docs.djangoproject.com/en/2.2/intro/tutorial01/) to get our feet wet in Django framework.

## To Run Locally
1. go to the __mysite__ directory in the terminal
2. ```$ python3 manage.py runserver```

## Table Of Contents:
1. [Page 1](#page1):
    - [Creating A Project](#CreatingAProject)
    - [Creating An App](#CreatingAnApp)
    - [path](#path)
2. [Page2](#page2):
    - [Database Setup](#DatabaseSetup)
    - [Creating Models](#CreatingModels)
    - [Django Admin](#DjangoAdmin)
    - [Development Server](#DevelopmentServer)
    - [Making App Modifiable by Admins](MakingAppModifiableByAdmins)
3. [Page3](#page3):
    - [Writing Views](#WritingViews)
    - [Write Views That Actually Do Something](#ViewsThatDoSomething)

## NOTES FROM THIS TUTORIAL
<a name="page1"></a>
## [Page 1](https://docs.djangoproject.com/en/2.2/intro/tutorial01/) Creating A Project -> Creating An App

### Creating A Project <a name="CreatingAProject"></a>

    ```
    $ django-admin startproject mysite //where mysite is the name of the project's directory
    ``` 

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
    
### Creating An App <a name="CreatingAnApp"></a>
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

    ```$ python manage.py runserver```
### path() <a name="path"></a>
- The __path()__ function is passed four arguments, two reuired: __route__ and __view__, and two optionals: __kwargs__, and __name__
    __REQUIRED__
    - __route__ - is a string that contains a URL pattern. When processing a request, Django starts at the first pattern in __urlpatterns__ and makes its way down the list, comparing the requested URL against each pattern until it finds one that matches.
        - Patterns don’t search GET and POST parameters, or the domain name. For example, in a request to https://www.example.com/myapp/, the URLconf will look for myapp/. In a request to https://www.example.com/myapp/?page=3, the URLconf will also look for myapp/
    - __view__ - When Django finds a matching pattern, it calls the specified view function with an __HttpRequest__ object as the first argument and any “captured” values from the route as keyword arguments
    __OPTIONAL__
    - __kwargs__ - _arbitrary keyword arguments_ can be passed in a dictionary to the target view
    - __name__ - _naming your URL lets you refer to it unambiguously from elsewhere_ in Django, especially from within templates. This powerful feature allows you to make global changes to the URL patterns of your project while only touching a single file.


<a name="page2"></a>

## [Page 2](https://docs.djangoproject.com/en/2.2/intro/tutorial02/) Database Setup -> Creating Models -> Django Admin -> Development Server -> Making App Modifiable by Admins
### Database Setup <a name="DatabaseSetup"></a>
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
### Creating Models <a name="CreatingModels"></a>
- __Migrations__ are Django's way of communicating changes you make to your models (adding a field, deleting a model, etc.) into your database schema
- A __model__ is the single, definitive source of truth about your data which contains __fields__ and __behaviors__ of the data you're storing. Django follows DRY principle and has the goal to define your data model in one place and automatically derive things from it.
    - checkout /polls/models.py to see an example of model
    - ForeinKey tells Django that each Choice is related to a single Question
- The code below allow us to do the following
    ```
    #polls/models.py¶
    from django.db import models

    class Question(models.Model):
        question_text = models.CharField(max_length=200)
        pub_date = models.DateTimeField('date published')

    class Choice(models.Model):
        question = models.ForeignKey(Question, on_delete=models.CASCADE)
        choice_text = models.CharField(max_length=200)
        votes = models.IntegerField(default=0)
    ```
    1. Create a database schema (CREATE TABLE statements) for this app.
    2. Create a Python database-access API for __accessing Question__ and __Choice__ objects.

### Activating Models
- After creating the model, we need to tell our project that __polls app__ is installed by __adding a reference to its configuration class__ in the INSTALLED_APPS setting in __mysite/settings.py__ file. The dotted path yhat you will add inside the INSTALLED_APPS array of apps is ```'polls.apps.PollsConfig'```
- Now that Django knows to include the __polls__ app, we can now run the following command:
    ``` $ python3 manage.py makemigrations polls```
    - __makemigrations__ tells Django that you've made some changes to your models and that you'd like the changes to be stored as a _migration_
    - __migrations__ are how Django stores changes to your models (database scehma)
- ```$ python3 manage.py sqlmigrate polls 0001``` - command that will run the migrations and manage your database schema automatically - that's called migrate
- ```$ python3 manage.py check``` - checks for any problems in your project without making migrations or touching the database
- ```$ python3 manage.py migrate``` - creates those tables in your database
    - __migrate__ command takes all the migrations that haven't been applied and runs them against your database _live, without losing data_, and essentially synchonizing the changes you made to your models with the schema in the database
    - migrations are very powerful and let you change/update your models over time without losing any of your data
    - __IMPORTANT__ to also run the following commands in __models.py__:
        ```
        $ python3 manage.py makemigrations
        $ python3 manage.py migrate
        ```
        - there are separate commands to make and apply migrations because you'll __commit migrations to your version control system and ship them with your app; making development easier and usable by other developers and in production__

### Playing with the API
- ```python3 manage.py shell``` - runs the Python shell interactive
- Add ```__str__()``` method that provides convenience when dealing with interactive prompt, but also for object's representation which is used throughout Django's automatically-generated admin
    ```
    def __str__(self):
        return self.question_text
    ```` 

### Introducing the Django Admin <a name="DjangoAdmin"></a>
- Django automates creation of admin interfaces for models; with a very clear separation between “content publishers” and the “public” site
1. Create an admin who can login to the admin site by running this command: 
    ```
    $ python manage.py createsuperuser
    ```
2. Enter desired username
3. Enter desired email
4. Enter password twice

### Start Development Server <a name="DevelopmentServer"></a>
- The Django admin site is activated by default, but if the server is not running start it like so:
    ```
    $ python manage.py runserver
    ```

### Make the poll app modifiable in the admin¶ <a name="MakingAppModifiableByAdmins"></a>
- tell the admin that Question objects have an admin interface by importing and registering Question __polls/admin.py__:
    ```
    # polls/admin.py¶
    from django.contrib import admin
    from .models import Question

    admin.site.register(Question)
    ```


<a name="page3"></a>

## [Page 3](https://docs.djangoproject.com/en/2.2/intro/tutorial03/)
- __view__ is a “type” of Web page in your Django application that generally serves a specific function and has a specific template
    - in this poll application, we'll have 4 views:
        1. Question __index__ - displays the latest few questions
        2. Question __detail__ - displays a question text, with no result but with a form to vote
        3. Question __results__ - displays results for a particular question
        4. Vote action - handles voting for a particular choice in a particular question
- __URL pattern__ is the general form of a URL - /newsarchive/<year>/<month>/
- __URLconfs__ maps URL patterns to views; meaning it is used in order to get from a URL to a view. Refer to [URL dispatcher](https://docs.djangoproject.com/en/2.2/topics/http/urls/) for more info

### Writing more views <a name="WritingViews"></a>
- add a few views in __polls/views.py__ that takes a question_id argument
```
#polls/views.py¶
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
```
- wire these new views into the __polls.urls__ module by addig the following __path()__ calls
```
#polls/urls.py¶
from django.urls import path
from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
```
- __NOTE__ When somebody requests a page from your website - like __"/polls/24/"__, Django will load the __mysite/urls.py__ because it's pointed to by the __ROOT_URLCONF__ in mysite/settings.py. Then it finds the variable named __urlpatterns__ which is a list of our paths and traverses the patterns in order until it finds a match at '__polls/__'. Then it strips off the mathcing text __("polls/")__ and sends the remaining text - __"34/"__ to the '__polls/urls.py__' URLConf for further processing. Then it matches '__<<int:question_id>>/__', resulting in a call to the __detail()__ view like so:
    ```
    detail(request=<HttpRequest object>, question_id=24)
    ```
    The __question_id=24__ part comes from __<<int:question_id>>__. Using angle brackets "captures" part of the URL and sends it as a keyword argument to the view function. The __:question_id>__ part of the string defines the name that will be used to identify the matched pattern, and the __<int:__ part is a converter that determines what patterns should match this part of the URL path.

### Write views that actually do something <a name="ViewsThatDoSomething"></a>
- Each view is responsible for doing one of two things:
    1. returning an __HttpResponse__ object containing the object for the requested page
    2. raising an __exception__ such as __Http404__
- new index() for __polls/views.py__
    ```
    #polls/views.py¶
    from django.http import HttpResponse
    from .models import Question

    def index(request):
        latest_question_list = Question.objects.order_by('-pub_date')[:5] #grab 5 most recent questions contained in an array
        output = ', '.join([q.question_text for q in latest_question_list]) #get each Question's text contained in a string and separated by a comma
        return HttpResponse(output) # Leave the rest of the views (detail, results, vote) unchanged
    ```
- create a __templates__ directory inside polls directory as Django will look for templates in there. Inside the templates directory, create a __polls__ directory with a __index.html__ file inside it.
- because of how __app_directories__ template loader works, you can refer to this template within Django simply as __polls/index.html__
- __Template namespacing__ - putting those templates inside another directory named for the application itself in order to ensure that we are pointing Django at the right directory. That is why the step above this is important becaus as Django will choose the first template it finds who name matches, and if you have a template with the same name in a different application, Django will be unable to distinguish between them.
    ```
    <!-- polls/templates/polls/index.html¶ -->
    {% if latest_question_list %}
        <ul>
        {% for question in latest_question_list %}
            <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
        {% endfor %}
        </ul>
    {% else %}
        <p>No polls are available.</p>
    {% endif %}
    ```
