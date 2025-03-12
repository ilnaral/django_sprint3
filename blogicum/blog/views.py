from datetime import datetime

from django.shortcuts import get_object_or_404, render

from .constants import INDEX_PAGE_POSTS_COUNT
from .models import Category, Post


def posts(post_list=None):
    """Базовый queryset для фильтрации постов по умолчанию."""
    if post_list is None:
        post_list = Post.objects.all()
    """Посты из БД."""
    return post_list.select_related(
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
    post_list = posts()[:INDEX_PAGE_POSTS_COUNT]
    return render(request, 'blog/index.html', {'post_list': post_list})


def post_detail(request, post_id):
    """Детали поста."""
    post = get_object_or_404(posts(), pk=post_id)
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    """Посты категории."""
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    post_list = posts(category.posts.all())
    return render(request, 'blog/category.html', {
        'category': category,
        'post_list': post_list
    })
