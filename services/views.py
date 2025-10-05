from django.shortcuts import render, get_object_or_404
from .models import Service

def service_list(request):
    """List all services"""
    services = Service.objects.all()
    context = {
        'services': services
    }
    return render(request, 'services/service_list.html', context)

def service_detail(request, slug):
    """Detail view for a single service"""
    service = get_object_or_404(Service, slug=slug)
    
    # Get related projects for this service category
    from portfolio.models import Project
    related_projects = Project.objects.filter(
        category__in=[cat[0] for cat in Project.PROJECT_CATEGORY if service.title.lower() in cat[1].lower()]
    )[:3]
    
    services = Service.objects.all()

    context = {
        'service': service,
        'services': services,
        'related_projects': related_projects,
    }
    return render(request, 'services/service_detail.html', context)