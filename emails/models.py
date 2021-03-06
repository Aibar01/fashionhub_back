from django.db import models


class Email(models.Model):
    email = models.EmailField(unique=True)
    creation_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return '/'
