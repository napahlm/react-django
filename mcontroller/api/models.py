from django.db import models
import string
import random

def generate_unique_code():
    length = 6

    while True:
        # Creates a random code string
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        # Breaks out of the loop if it's unique
        if Room.objects.filter(code=code).count() == 0:
            break

    return code


# Models
# Storing information. The table is replaced by a model. A layer of abstraction for databases.

class Room(models.Model):                                               # inherits from models
    code = models.CharField(max_length=8, default=generate_unique_code, unique=True)      # Limits on codes
    host = models.CharField(max_length=50, unique=True)                 # Only one host AKA unique
    guest_can_pause = models.BooleanField(null=False, default=False)    # null=False means a value must be passed
    votes_to_skip = models.IntegerField(null=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True)                # Adds date and time created
