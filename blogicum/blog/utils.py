from django.utils import timezone

from .models import Post


def get_posts():
    """Получение опубликованных постов из БД."""
    return Post.objects.select_related(
        'category',
        'location',
        'author'
    ).filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=timezone.now()
    )
