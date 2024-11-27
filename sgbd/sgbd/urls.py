from django.contrib import admin
from django.urls import path, include
import django_browser_reload.urls  # Import des URLs de django-browser-reload
from auth_app.views import inscription
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', inscription, name='inscription'),  # URL pour l'inscription
    path('admin/', admin.site.urls),
    path('', include('auth_app.urls')),  # Inclure les URLs de auth_app
    path('__reload__/', include(django_browser_reload.urls)),  # URL pour le rechargement automatique
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
