"""myFAIR URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from . import views
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^$', views.index),
    url(r'^login', views.login),
    url(r'^logout$', views.logout),
    url(r'^upload', views.upload),
    url(r'^triples', views.triples),
    url(r'^store', views.store),
    url(r'^samples', views.samples),
    url(r'^modify', views.modify),
    url(r'^delete', views.delete),
    url(r'^results', views.show_results),
    url(r'^rerun', views.rerun_analysis),
    url(r'^history', views.store_history),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)