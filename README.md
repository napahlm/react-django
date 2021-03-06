# Web Development and Hosting

TODO: find bug preventing room joining. Fixed by going back to an earlier reactjs version.

## Setup

1) Clone the repository. Further setup is done in powershell.

2) Add missing settings with secret key in mcontroller/mcontroller/settings.py.

3) Set up venv in project-name and activate it.

```
py -m venv env
.\env\Scripts\activate
```

4) Install requirements in venv

```
pip install -r requirements.txt
```

5) Go into the project and make migrations and migrate to create database

```
cd .\mcontroller\
python .\manage.py makemigrations
python .\manage.py migrate
```

6) Test by running server.

```
python .\manage.py runserver
```

7) Check if npm works. In an activated venv, go to the frontend directory and run this command.

```
cd .\mcontroller\frontend\
npm run dev
```

8) If the last step results in "Module not found" or similar do the following:

In the frontend folder, delete node_modules and package-lock.json, then reinstall npm.

```
Remove-Item .\node_modules\ -Recurse
Remove-Item .\package-lock.json
npm install
npm run dev
```

### Creating a website with React and Django using Python
 
The purpose of the project is to get familiar with tools for full stack development by developing a web site from scratch.

Initial steps are done with the help of this great tutorial[^1].

### Hosting the website

The end goal of the project is to either host it as a personal portfolio or have some sort of function. Hosting alternatives have not yet been decided on.


## Summary of used tools

### React


Javascript library for building UIs.

### Django

High-level Python web framework.

### Google Cloud (?)

[???]


## Useful testing snippets

### Running the server locally

Locate the project in a powershell terminal.

```
cd react-django\mcontroller
```

Run the server.

```
python .\manage.py runserver
```


## Dependencies

node.js

venv dependencies:
django
djangorestnetwork

vscode addons:
Django
ES7 React
Javascript code snippets

## Backend structure [Default files omitted]

```
api/  
????????? urls.py  
????????? serializers.py  
```

## Frontend structure [Default files omitted]

Dependencies:
npm/node.js
Babel
react
material-ui

Frontend is managed as an app like the API/backend.

```
frontend/  
????????? node_modules/  
????????? src/  
???   ????????? components/  
???   ???   ????????? App.js  
???   ????????? index.js  
????????? static/  
???   ????????? css/  
???   ???   ????????? index.css [Styling the app]  
???   ????????? frontend/  
???   ????????? images/  
????????? templates/  
???   ????????? frontend/  
???       ????????? index.html  
????????? babel.config.json  
????????? package-lock.json  
????????? package.json  
????????? urls.py  
????????? webpack.config.js  
```

[^1]: https://www.youtube.com/watch?v=JD-age0BPVo&list=PLzMcBGfZo4-kCLWnGmK0jUBmGLaJxvi4j    