from django.shortcuts import render, get_object_or_404
from .models import Project

def project_list(request):
    """List all projects with filtering capability"""
    projects = Project.objects.all().order_by('-completion_date')
    
    # Filter by category if provided
    category_filter = request.GET.get('category')
    if category_filter:
        projects = projects.filter(category=category_filter)
    
    # Filter by technology if provided
    tech_filter = request.GET.get('technology')
    if tech_filter:
        projects = projects.filter(technologies_used__icontains=tech_filter)
    
    context = {
        'projects': projects,
        'categories': Project.PROJECT_CATEGORY,
        'selected_category': category_filter,
        'selected_technology': tech_filter,
    }
    return render(request, 'portfolio/project_list.html', context)

def project_detail(request, slug):
    """Detail view for a single project"""
    project = get_object_or_404(Project, slug=slug)
    
    # Get related projects (same category, excluding current project)
    related_projects = Project.objects.filter(
        category=project.category
    ).exclude(id=project.id)[:3]
    
    # Parse technologies used for display
    technologies = [tech.strip() for tech in project.technologies_used.split(',')]
    
    context = {
        'project': project,
        'related_projects': related_projects,
        'technologies': technologies,
    }
    return render(request, 'portfolio/project_detail.html', context)