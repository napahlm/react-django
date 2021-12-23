from django.urls import path
from .views import index

urlpatterns = [
    path('', index) # Renders template when a blank request is made
]
