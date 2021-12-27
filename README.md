# Web Development and Hosting

## Creating a website with React and Django using Python
 
The purpose of the project is to get familiar with tools for full stack development by developing a web site from scratch.

Initial steps are done with the help of this great tutorial[^1].

## Hosting the website

The end goal of the project is to either host it as a personal portfolio or have some sort of function. Hosting alternatives have not yet been decided on.


# Summary of used tools

## React

Javascript library for building UIs.

## Django

High-level Python web framework.

## Google Cloud (?)

[???]


# Useful testing snippets

## Running the server locally

Locate the project in a powershell terminal.

```
cd react-django\mcontroller
```

Run the server.

```
python .\manage.py runserver
```


# Dependencies

node.js

venv dependencies:
django
djangorestnetwork

vscode addons:
Django
ES7 React
Javascript code snippets

# Backend structure [Default files omitted]

```
api/  
├── urls.py  
└── serializers.py  
```

# Frontend structure [Default files omitted]

Dependencies:
npm/node.js
Babel
react
material-ui

Frontend is managed as an app like the API/backend.

```
frontend/  
├── node_modules/  
├── src/  
│   ├── components/  
│   │   └── App.js  
│   └── index.js  
├── static/  
│   ├── css/  
│   │   └── index.css [Styling the app]  
│   ├── frontend/  
│   └── images/  
├── templates/  
│   └── frontend/  
│       └── index.html  
├── babel.config.json  
├── package-lock.json  
├── package.json  
├── urls.py  
└── webpack.config.js  
```

[^1]: https://www.youtube.com/watch?v=JD-age0BPVo&list=PLzMcBGfZo4-kCLWnGmK0jUBmGLaJxvi4j    