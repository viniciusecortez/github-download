import requests
from django.shortcuts import render, redirect

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
            consume_github = form.save()
            file = open(consume_github.nome_do_arquivo, "wb")
            file.write(requests.get(consume_github.download_link).text)
            file.close()
            return redirect(consume_github.nome_do_arquivo)