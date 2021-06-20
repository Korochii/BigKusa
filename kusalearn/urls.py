"""kusalearn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# Use include() to add paths from the catalog application
from django.urls import include
from django.views.static import serve 
from django.conf.urls import url
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('accounts/', include('accounts.urls')),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]



urlpatterns += [
    path('home/', include('home.urls')),
]

urlpatterns += [
    path('log/', include('log.urls')),
]

urlpatterns += url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT})
    

from django.views.generic.base import TemplateView
urlpatterns += [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]
#Add URL maps to redirect the base URL to our application
#from django.views.generic import RedirectView
#urlpatterns += [
#    path('', RedirectView.as_view(url='home/', permanent=True)),
#]

# Use static() to add url mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
