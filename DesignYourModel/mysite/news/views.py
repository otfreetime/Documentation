from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from .models import Article


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def year_archive(request, year):
    a_list = Article.objects.filter(pub_date__year=year)
    context = {'year': year, 'article_list': a_list}
    return render(request, 'news/year_archive.html', context)