from django.db import models
from django.contrib.auth.models import User


class TodoItem(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    is_done = models.BooleanField(default=False)
    is_important = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False,
                                   related_name='todo_items')

    def __str__(self):
        return f'{self.title} - {self.description}'

    def save(self, *args, **kwargs):
        if self.is_done:
            self.is_important = False
        super(TodoItem, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created_at']
