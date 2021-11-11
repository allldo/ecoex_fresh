from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from landing.models import FAQ, News, Service

# Create your views here.


def main_page(request):
    context = {}
    context['Service'] = Service.objects.all()[:3]
    context['FAQ'] = FAQ.objects.all()[:3]
    context['Latest_News'] = News.objects.all()[:3]
    return render(request, 'landing/main_page.html', context)


def news_detail_page(request, news_slug):
    context={}
    context['Exact_news'] = get_object_or_404(News, slug=news_slug)
    return render(request, 'news/news_detail.html', context)


def faq_list_page(request):
    context = {}
    context['FAQS'] = FAQ.objects.all()
    return render(request, 'faq/faq_list_page.html', context)


def news_list_page(request):
    context = {}
    page = request.GET.get('page', 1)  
    paginator = Paginator(News.objects.all().order_by('-date'), 1)

    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)
    context['NEWS'] = news
    return render(request, 'news/news_list_page.html', context)


def contacts(request):
    context ={}
    return render(request, 'landing/contacts.html', context)