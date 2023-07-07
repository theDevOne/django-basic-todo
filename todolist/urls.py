from django.urls import path
from . import views

urlpatterns = [
    path('', views.TodoListView.as_view(), name="todo_list"),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('view/<int:pk>/', views.view_todo_item, name='view_todo_item'),
    path('create/', views.create_todo_item, name='create_todo_item'),
    path('edit/<int:pk>/', views.edit_todo_item, name='edit_todo_item'),
    path('delete/<int:pk>/', views.delete_todo_item, name='delete_todo_item'),
]
