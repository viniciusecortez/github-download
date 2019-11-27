from django.shortcuts import render

# Create your views here.
from django.views.decorators.http import require_GET

from main_app.forms import MainForm


def index(request):
    if request.method == 'GET':
        form = MainForm()
        return render(request, 'main_app/index.html', {'form': form})
    else:
        form = MainForm(request.POST)
        if form.is_valid():
            obj = form.save()
            

