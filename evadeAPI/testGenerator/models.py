from django.db import models

class Evader_test(models.Model):

    title = models.CharField(
        max_length=60,
        help_text=('Required. 60 characters or fewer.'))
    description = models.CharField(
        max_length=150,
        help_text=('Required. 150 characters or fewer.'),
        default='')

    def __str__(self):
        return self.title