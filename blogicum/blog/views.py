from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Post, Category


def posts():
    """Получение постов из БД"""
    return Post.objects.select_related(
        'category',
        'location',
        'author'
    ).filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=timezone.now()
    )


def index(request):
    """Главная страница"""
    return render(
        request,
        'blog/index.html',
        {'post_list': posts().order_by('-pub_date')[:5]}
    )


def post_detail(request, pk):
    """Отображение полного описания выбранной записи"""
    post = get_object_or_404(posts(), pk=pk)
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    """Отображение публикаций категории"""
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    post_list = posts().filter(category=category).order_by('-pub_date')

    context = {
        'category': category,
        'post_list': post_list
    }
    return render(request, 'blog/category.html', context)
