from django import forms

class TaskForm(forms.Form):
    description = forms.CharField(label='Add task', max_length=255)
