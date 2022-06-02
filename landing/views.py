from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from ecology_full_new import settings
from landing.models import FAQ, News, Service, PassDocs, ServiceGroup, AboutUs

# Create your views here.


def main_page(request):
    context = {}
    context['Service'] = Service.objects.all()[5:8]
    context['FAQ'] = FAQ.objects.all()[:3]
    context['Latest_News'] = News.objects.all()[:3]
    return render(request, 'landing/main_page.html', context)


def news_detail_page(request, news_slug):
    context={}
    context['Exact_news'] = get_object_or_404(News, slug=news_slug)
    context['recent'] = News.objects.all()[:3]
    return render(request, 'news/news_detail.html', context)


def faq_list_page(request):
    context = {}
    context['FAQS'] = FAQ.objects.all()
    return render(request, 'faq/faq_list_page.html', context)


def news_list_page(request):
    context = {}
    page = request.GET.get('page', 1)  
    paginator = Paginator(News.objects.all().order_by('-date'), 4)

    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)
    context['NEWS'] = news

    return render(request, 'news/news_list_page.html', context)


def news_search(request):
    context = {}
    page = request.GET.get('page', 1)

    if 'q' in request.GET:
        query = request.GET.get('q')
        paginator = Paginator(News.objects.filter(Q(title__icontains=query)).order_by('-date'), 1)
        try:
            news = paginator.page(page)
        except PageNotAnInteger:
            news = paginator.page(1)
        except EmptyPage:
            news = paginator.page(paginator.num_pages)
        context['NEWS'] = news
        return render(request, 'news/news_search.html', context)


def service_detail(request, service_id):
    service_object = get_object_or_404(Service, id=service_id)
    context = {}
    context['service_obj'] = service_object
    return render(request, 'service/service_detail.html', context)


def contacts(request):
    context ={}
    return render(request, 'landing/contacts.html', context)


def pass_docs(request):
    context = {}
    docs = PassDocs.objects.all()
    context['docs'] = docs
    context['rng'] = ['1','1','1','1','1','1','1','1']
    return render(request, "landing/pass_docs.html", context)


def services(request):
    context = {'Services': Service.objects.all(), 'Services_group': ServiceGroup.objects.all()}
    return render(request, "service/services_list.html", context)


def form_valid(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest' and request.method == 'POST':
        message = f'Имя: {request.POST.get("k3k3r")}\nНомер телефона человека: {request.POST.get("number_of_phone")}\nЕго сообщение: {request.POST.get("message")}'
        send_mail(
            'Сообщение с сайта',
            message,
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )
    return JsonResponse({
        'fucking cumming': 'fucking cumming'
    })


def about_us(request):
    context = {'about_us': AboutUs.objects.first()}
    return render(request, 'landing/aboutUs.html', context)


def privacy(request):
    return render(request, 'landing/privacy.html')


# Error pages


def handler404(request, exception, template_name="error/404.html"):
    response = render(request, template_name)
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    return render(request, 'error/500.html', status=500)


def handler403(request, exception):
    response = render(request, 'error/403.html', status=403)
    return response
