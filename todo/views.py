from urllib.parse import _NetlocResultMixinBytes
from django.shortcuts import render, redirect
from django.views import View

from todo.models import Task, Note
from todo.forms import TaskForm, NoteForm


class TodoListView(View):
    def get(self, request):
        '''GET the todo list homepage, listing all tasks in reverse order that they were created'''
        tasks = Task.objects.all().order_by('-id')
        form = TaskForm()

        return render(
            request=request, template_name = 'list.html', context = {'tasks': tasks, 'form': form}
        )

    def post(self, request):
        '''POST the data in the from submitted by the user, creating a new task in the todo list'''
        form=TaskForm(request.POST)
        if form.is_valid():
            task_description = form.cleaned_data['description']
            Task.objects.create(description=task_description)

        # "redirect" to the todo homepage
        return redirect('todo_list')


class TodoDetailView(View):
    def get(self, request, task_id):
        '''GET the detail view of a single task on the todo list'''
        task = Task.objects.get(id=task_id)
        form = TaskForm(initial={'description': task.description})
        return render(
            request=request, template_name='detail.html', context={'form':form, 'id': task_id}
        )

    def post(self, request, task_id):
        '''Update or delete the specific task based on what the user submitted in the form'''
        task = Task.objects.filter(id=task_id)
        if 'save' in request.POST:
            form = TaskForm(request.POST)
            if form.is_valid():
                task_description = form.cleaned_data['description']
                task.update(description=task_description)
        elif 'delete' in request.POST:
            task.delete()

        # "redirect" to the todo homepage
        return redirect('todo_list')

    def post(self, request, task_id):
        task = Task.objects.filter(id=task_id)
        if 'complete' in request.POST:
             form = TaskForm(request.POST)
             if form.is_valid():
                task.update(completed = True)

        # "redirect" to the todo homepage
        return redirect('todo_list')
            


class NoteView(View):
    def get(self, request):
        '''GET the todo list homepage, listing all tasks in reverse order that they were created'''
        notes = Note.objects.all().order_by('text')
        form = NoteForm()

        return render(
            request=request, template_name = 'notes.html', context = {'notes': notes, 'form': form}
        )

    def post(self, request):
        '''POST the data in the from submitted by the user, creating a new task in the todo list'''
        form=NoteForm(request.POST)
        if form.is_valid():
            note_text = form.cleaned_data['text']
            Note.objects.create(text=note_text)

        # "redirect" to the todo homepage
        return redirect('notes')