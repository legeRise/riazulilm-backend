from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    

    USERNAME_FIELD = 'email'       # email is now used to log in
    username = None
    REQUIRED_FIELDS = []           # AbstractUser by default sets 'email' in REQUIRED_FIELDS, but when we have set email as USERNAME_FIELD, we don't need it in REQUIRED_FIELDS

    objects = CustomUserManager()  
    
    def __str__(self):
        return self.email