from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('services/', include('services.urls')),
    path('portfolio/', include('portfolio.urls')),
    path('blog/', include('blog.urls')),
    path('contact/', include('contacts.urls')),
]

# This is only for development. In production, serve media files with your web server.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)