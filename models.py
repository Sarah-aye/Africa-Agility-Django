from django.db import models



class todoItem(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

# Create your models here.
 