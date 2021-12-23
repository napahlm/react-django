from django.shortcuts import render

# Create your views here.

# Render index

def index(request, *args, **kwargs):
    return render(request, 'frontend/index.html')