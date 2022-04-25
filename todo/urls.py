from django.urls import path
from todo.views import TodoDetailView, TodoListView

urlpatterns = [
    path('', TodoListView.as_view(), name='todo_list'),
    path('<int:task_id>', TodoDetailView.as_view(), name='task')
]
