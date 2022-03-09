from django.db import models
import string
import random
# fat models, thin views

def generate_unique_code():
    length = 6

    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if Room.objects.filter(code=code).count() == 0:
            break

    return code

# Create your models here.
class Room(models.Model):
    code = models.CharField(max_length=8, default="", unique=True) # room seed
    host = models.CharField(max_length=8, unique=True) # host id?
    guest_can_pause = models.BooleanField(null=False, default=True)
    votes_to_skip = models.IntegerField(null=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
