from .models import News


def news(request):
    return {'RecentNews': News.objects.all()[:3]}

