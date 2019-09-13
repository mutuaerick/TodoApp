from django.db import models

from django.utils import timezone

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class TodoList(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now=True, blank=True, null=False)
    date_due = models.DateTimeField(auto_now=False, blank=True, null=False)
    category = models.ForeignKey(Category, default="general", on_delete=None)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title