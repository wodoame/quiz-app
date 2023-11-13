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


2. Now that the virtual environment created, navigate to the repository where the `requirements.txt` file is located and run the command:
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
   

   
  
