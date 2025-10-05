from django.shortcuts import render
from portfolio.models import Project
from services.models import Service
from blog.models import Post

def home(request):
    """Homepage view"""
    featured_projects = Project.objects.filter(is_featured=True)[:3]
    services = Service.objects.all()[:6]
    recent_posts = Post.objects.filter(published=True).order_by('-created_at')[:3]
    
    context = {
        'featured_projects': featured_projects,
        'services': services,
        'recent_posts': recent_posts,
    }
    return render(request, 'core/home.html', context)

def about(request):
    """About page view"""
    team_members = [
        {
            'name': 'Your Name',
            'position': 'Founder & Lead Developer',
            'bio': 'Experienced full-stack developer with expertise in Django, Python, and modern web technologies.',
            'photo': '/static/images/team/placeholder.jpg'  # Add actual photos later
        },
        # Add more team members as needed
    ]
    services = Service.objects.all()
    context = {
        'team_members': team_members,
        'services': services,
        
    }
    return render(request, 'core/about.html', context)

def privacy_policy(request):
    """Privacy policy page"""
    return render(request, 'core/privacy_policy.html')

def terms_of_service(request):
    """Terms of service page"""
    return render(request, 'core/terms_of_service.html')