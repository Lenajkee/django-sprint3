from django.shortcuts import get_object_or_404, render

from .models import Category
from .utils import get_posts

POSTS_COUNT_ON_INDEX = 5


def index(request):
    """Главная страница."""
    post_list = get_posts().order_by('-pub_date')[:POSTS_COUNT_ON_INDEX]
    return render(
        request,
        'blog/index.html',
        {'post_list': post_list}
    )


def post_detail(request, post_id):
    """Отображение полного описания выбранной записи."""
    post = get_object_or_404(get_posts(), pk=post_id)
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    """Отображение публикаций категории."""
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    post_list = get_posts().filter(category=category).order_by('-pub_date')

    context = {
        'category': category,
        'post_list': post_list
    }
    return render(request, 'blog/category.html', context)
