from django.http import FileResponse
from django.shortcuts import render
from pathlib import Path
from os import path

BASE_DIR = Path(__file__).resolve().parent.parent


def home_view(request):
    return render(request, 'home_page/home.html')


def about_view(request):
    return render(request, 'home_page/about.html')


def resume_view(request):
    # resume_filepath = path.join(BASE_DIR, 'static/media/texts/resume.pdf')
    # try:
    #     return FileResponse(open(resume_filepath, 'rb'), content_type='application/pdf')
    # except FileNotFoundError:
    #     print('someting broked')
    return render(request, 'home_page/resume.html')
