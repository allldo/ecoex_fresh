from django.shortcuts import get_object_or_404, render

from landing.models import FAQ, News, Service

# Create your views here.


def main_page(request):
    context = {}
    context['Service'] = Service.objects.all()
    context['FAQ'] = FAQ.objects.all()
    context['Latest_News'] = News.objects.all()
    return render(request, 'landing/main_page.html', context)


def news_detail_page(request, slug):
    context={}
    context['Exact_news'] = get_object_or_404(News, slug=slug)
    return render(request, 'news/news_detail.html', context)