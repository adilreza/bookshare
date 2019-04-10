"""booklovers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
#test


#test


from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from Blovers.views import home
from Blovers.views import registration
from Blovers.views import login
from Blovers.views import test
from Blovers.views import mainpage
from Blovers.views import userpanel
from Blovers.views import logout
from Blovers.views import postabook
from Blovers.views import uploadonline
from Blovers.views import details_selected

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', test, name="test"),
    path('home/', home, name="home"),
    path('mainpage/', mainpage, name="mainpage"),
    path('registration/', registration, name="registration"),
    path('login/', login, name="login"),
    path('userpanel/', userpanel, name="userpanel"),
    path('logout/', logout, name="logout"),
    path('postabook/', postabook, name="postabook"),
    path('uploadonline/', uploadonline, name="uploadonline"),
    path('details_selected/', details_selected, name="details_selected"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
