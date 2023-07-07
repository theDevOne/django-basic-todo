from django.contrib import admin
from .models import TodoItem

# Register your models here.
@admin.register(TodoItem)
class TodoItemAdmin(admin.ModelAdmin):
    list_display = ('name','completed')
    list_filter = ('user', )
    search_fields = ('name', 'user__username')