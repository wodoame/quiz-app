# Prerequisites 
1. You need to have python installed as the backend uses python. You can visit https://www.python.org/downloads to download and install python
2. You also need to have pulled this repository down onto your computer.

# Setting up a virtual environment
- A virtual environment is a container that holds all python requirements or dependencies for the project
- To be able to run the project you need to install the project requirements
- The python dependencies are inside a file called `requirements.txt` which is located in the root directory of the repository
- Navigate to a directory where you want the virtual environment folder to live (You can keep it on your desktop if you like)
- To create the virtual environment open cmd and type
  
    ```
    python -m venv quizapp-environment
    ```
- A folder should be created with the name of `quizapp-environment` in the directory you chose to create the environment in.
- Note that the virtual environment doesn't have to be inside the repository. It can live anywhere on your computer as long as you can find it.
  
# Activating the virtual environment and installing project requirements
- Now the virtual environment in installed we have to install some dependencies inside the environment and we will do so with the help of `requirements.txt`

1. First activate the virtual environment so that your computer knows you are inside of it. Open cmd and go to `Scripts` directory inside the `quizapp-environment` and type `activate`
   It should look something like this:
    ```
    C:\Users\HP\Desktop\quizzapp-environment\Scripts>activate
    ```
    After this you should see the environment name inside a bracket preceding the current directory path like this:
 
    ```
      (quizzapp-environment)C:\Users\HP\Desktop\quizzapp-environment\Scripts>
    ```


2. Now that the virtual environment is activated, navigate to the repository where the `requirements.txt` file is located and run the command:
   ```
   pip install -r requirements.txt
   ```
   This will install all the dependencies for the project

# File structure
- Django (our backend technology) just like other frameworks has a file structure we need to follow.
- All Html files should be placed inside the `templates` directory. From the root directory the path is `core/templates`
- Now static files (images, javascript, css and other stuff you link to your html) should be placed inside the `static` directory. From the root directory the path is `core/static`.
- Quick note: javascript inside the html is allowed if you find it necessary to do so.
- Now you may want to organize your html and css files into folders and you can do that as long as all those folders are inside the required directories (`templates` and `static`).
- Why do we need to do this ? First of all it is necessary so that data can be passed to the html documents from the backend. Second, the backend needs that to be able to process the static files.
- When we get the point where we need to use the Django server to run the html pages you'll see how it works. But for the mean time you can run the html files without the Django server
  while maintaining the appropriate directories

# Running the Django server
- To integrate our backend with the frontend our html pages have to be rendered from the backend as opposed to just clicking on the html file.
- Whenever you are going to write code you need to run the server since it enable the html pages to be rendered.
- To start the django server you first need to activate the virtual environment. I explained how to do that in a previous section so you can refer to that.
- Navigate to the root directory of the repository where the `manage.py` file is found.
- In cmd you type
  
  ```
  python manage.py migrate
  ```
- After that you type
  
  ```
  python manage.py runserver
  ```
- Now before running the server you would have told me the html page you are going to work on and in which folder it will be in. Why this ? This is because I have to write python code to allow that particular
  page to be rendered. It won't be necessary to show that code here.
- I will do this in such a way that when you type `http://127.0.0.1:8000/the-page-name-without-dot-html-extension` the page should load in the browser. The server will have to be running of course.
- So for now just run the server and see whether it works. How do you know that it worked ? Well you should see something like this in the terminal:

  ```
  Watching for file changes with StatReloader
  Performing system checks...
  
  System check identified no issues (0 silenced).
  November 14, 2023 - 17:11:57
  Django version 4.2.2, using settings 'quizapp.settings'
  Starting development server at http://127.0.0.1:8000/
  Quit the server with CTRL-BREAK.
  ```
- Exit the terminal. 
  

   
  
