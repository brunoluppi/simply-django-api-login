from django.db import models

class User(models.Model):
    user_id = models.CharField(max_length=255, primary_key=True)
    user_name = models.CharField(max_length=150, default='')
    user_email = models.EmailField(default='')
    user_password = models.CharField(max_length=255, default='')
    user_token = models.CharField(max_length=255, default='')

    def __str__(self):
        return f'ID: {self.user_id} |User: {self.user_name} | E-mail: {self.user_email} | Pass Hash: {self.user_password} | Token: {self.user_token} '