from django.db import models
from unittest.util import _MAX_LENGTH

# Create your models here.

class ChatRoom(models.Model):
    key_no = models.CharField(max_length=100)
    name = models.CharField(max_length=300)
    create_time = models.DateTimeField('date published')
    
    def __str__(self):
        return self.name