from django.db import models

class Data(models.Model):
    message = models.TextField(default='0000000')
    date = models.TextField(default='0000000')

    class Meta:
        db_table = "info"