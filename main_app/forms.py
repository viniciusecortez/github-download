from django.forms import forms, CharField

from main_app.models import ConsumeGithub


class MainForm(forms.Form):
    user = CharField(max_length=30)
    repository = CharField(max_length=40)
    path = CharField(max_length=400)

    def save(self):
        return ConsumeGithub(self.cleaned_data['user'], self.cleaned_data['repository'], self.cleaned_data['path'])
