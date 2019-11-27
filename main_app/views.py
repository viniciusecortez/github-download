import os

import requests
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
# Create your views here.
from django.views.decorators.http import require_GET

from github_download import settings
from main_app.forms import MainForm


def index(request):
    if request.method == 'GET':
        form = MainForm()
        return render(request, 'main_app/index.html', {'form': form})
    else:
        form = MainForm(request.POST)
        if form.is_valid():
            consume_github = form.save()
            arq_text = requests.get(consume_github.download_link).text
            file = open(consume_github.nome_do_arquivo, "w")
            file.write(arq_text)
            file.close()
            return redirect(f'download/{consume_github.nome_do_arquivo}')


def download(request, file):
    file_path = os.path.join(settings.BASE_DIR, file)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/txt")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404
