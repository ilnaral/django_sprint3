from datetime import datetime

from django.utils import timezone
from django.shortcuts import render, get_object_or_404

from .models import Post, Category


def posts():
    """Посты из БД."""
    return Post.objects.select_related(
        'category',
        'location',
        'author'
    ).filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=datetime.now()
    )


def index(request):
    """Лента записей."""
    return render(request, 'blog/index.html', {'post_list': posts()[:5]})


def post_detail(request, post_id):
    """Полный/детальный текст поста."""
    post = get_object_or_404(posts(), pk=post_id)
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    """Показ публикации по определенной категории."""
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    post_list = category.posts.filter(
        is_published=True,
        pub_date__lte=timezone.now()
    )
    context = {'category': category, 'post_list': post_list}
    return render(request, 'blog/category.html', context)
