"""dealio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from deals import views as deal_view
from django.conf import settings
from django.conf.urls.static import static
from deals.views import search
from deals.views import custom_error
from deals.views import terms
from deals.views import help_page
from deals.views import privacy_policy

urlpatterns = [
    url(r'^deal/(.*)$', deal_view.deal),
    url(r'^$', deal_view.index),
    path('admin/', admin.site.urls),
    url(r'^search/$', search, name="search"),
    url(r'^error/$', custom_error, name="error"),
    url(r'^terms/$', terms, name="terms"),
    url(r'^help_page/$', help_page, name="help_page"),
    url(r'^privacy_policy/$', privacy_policy, name="privacy_policy")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
              + static(settings.STATIC_URL, document_root=settings.STATIC_URL)
