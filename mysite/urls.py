"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from app import views as app
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    path('user/new', app.UserNewView.as_view(), name = 'user-create'),

    path('login/travel-list', app.TravelListView.as_view(), name = 'travel-list'),

    path('login/travel-list/addviagem', app.TravelNewView.as_view(), name = 'travel-create'),

    path('login/travel-list/minhasviagens', app.TemplateMinhasViagens.as_view(), name = 'minhasviagens'),

    path('login/travel-list/viagensmeusamigos', app.TemplateViagensamigos.as_view(), name = 'viagensamigos'),

    path('travels/new', app.TravelNewView.as_view(), name = 'travel-create'),

    path('travel/<int:pk>/edit', app.TravelUpdateView.as_view(), name = 'travel-update'),

    path('services/', app.TemplateService.as_view(), name = 'services'),

    path('login/', app.TemplateLogin.as_view(), name = 'login'),

    path('', app.TemplateInicial.as_view(), name = 'initial'),

]