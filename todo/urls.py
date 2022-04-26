from django.urls import path
from todo.views import TodoDetailView, TodoListView, NoteView

urlpatterns = [
    path('', TodoListView.as_view(), name='todo_list'),
    path('<int:task_id>', TodoDetailView.as_view(), name='task'),
    path('notes', NoteView.as_view(), name='notes')
    
]
