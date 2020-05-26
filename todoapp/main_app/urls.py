from django.urls import path
from . import views

app_name = 'main_app'
urlpatterns = [
    path('', views.ToDoListView.as_view(), name='home'),
    path('add/', views.ToDoCreateView.as_view(), name='add'),
    path('delete_todo/<int:todo_id>', views.delete_todo, name='delete')
]