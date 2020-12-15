from django.shortcuts import render
from django.views.generic import DetailView
from .models import article


def Home_view(request):
    articles = article.objects.all()
    return render(request, 'index.html', {'articles': articles})


def List_view(request):
    articles = article.objects.all()
    return render(request, 'story.html', {'articles': articles})


class Detail_view(DetailView):
    template_name = 'detail.html'
    queryset = article.objects.all()
