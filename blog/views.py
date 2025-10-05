from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post, models
from services.models import Service

def post_list(request):
    """List all published blog posts with pagination"""
    posts_list = Post.objects.filter(published=True).order_by('-published_date')
    services = Service.objects.all()
    # Pagination
    paginator = Paginator(posts_list, 6)  # 6 posts per page
    page = request.GET.get('page')
    
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    
    context = {
        'posts': posts,
        'services': services,
    }
    return render(request, 'blog/post_list.html', context)

def post_detail(request, slug):
    """Detail view for a single blog post"""
    post = get_object_or_404(Post, slug=slug, published=True)
    
    # Get related posts (same author or similar tags)
    related_posts = Post.objects.filter(
        published=True
    ).exclude(id=post.id).order_by('-published_date')[:3]
    
    context = {
        'post': post,
        'related_posts': related_posts,
    }
    return render(request, 'blog/post_detail.html', context)

def post_search(request):
    """Search functionality for blog posts"""
    query = request.GET.get('q')
    posts = Post.objects.filter(published=True).order_by('-published_date')
    
    if query:
        posts = posts.filter(
            models.Q(title__icontains=query) |
            models.Q(content__icontains=query) |
            models.Q(excerpt__icontains=query)
        )
    services = Service.objects.all()
    context = {
        'posts': posts,
        'query': query,
        'services': services,
    }
    return render(request, 'blog/post_search.html', context)