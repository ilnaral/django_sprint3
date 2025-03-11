from datetime import datetime

from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .constants import INDEX_PAGE_POSTS_COUNT
from .models import Category, Post


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
    post_list = posts()[:INDEX_PAGE_POSTS_COUNT]
    return render(request, 'blog/index.html', {'post_list': post_list})


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
    all_posts = category.posts.all()
    context = {'category': category,
               'post_list': post_list,
               'all_posts': all_posts}
    return render(request, 'blog/category.html', context)
