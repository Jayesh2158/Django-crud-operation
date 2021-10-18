from django.db import models

class list(models.Model):
    item = models.CharField(max_length=100)
    complete = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.item 
