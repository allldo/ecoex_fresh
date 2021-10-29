from django.shortcuts import get_object_or_404, render

from landing.models import FAQ, News, Service

# Create your views here.


def main_page(request):
    context = {}
    context['Service'] = Service.objects.all()[:3]
    context['FAQ'] = FAQ.objects.all()[:3]
    context['Latest_News'] = News.objects.all()[:3]
    return render(request, 'landing/main_page.html', context)


def news_detail_page(request, news_slug):
    print('qwe')
    context={}
    context['Exact_news'] = get_object_or_404(News, slug=news_slug)
    return render(request, 'news/news_detail.html', context)