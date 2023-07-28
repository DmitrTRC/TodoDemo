from django.contrib import admin
from todo.models.mtodo import TodoItem


@admin.register(TodoItem)
class TodoItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'is_done', 'is_important', 'created_at', 'updated_at', 'created_by')
