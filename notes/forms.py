from django import forms

from notes.models import Task

class TaskForm(forms.ModelForm):

    class Meta:

        model = Task

        # fields = "__all__"

        exclude = ("created_date","status","updated_date")

        widgets = {
            "title":forms.TextInput(attrs={"class":"form-control"}),

            "description":forms.Textarea(attrs={"class":"form-control"}),

            "due_date":forms.DateInput(attrs={"class":"form-control","type":"date"}),

            "category":forms.Select(attrs={"class":"form-control form-select"}),

            "user":forms.TextInput(attrs={"class":"form-control"})
        }