"""std_mgnt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from std_mgnt import views,HOD_views,staff_views,student_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home),
    #profile
    path('profile/',views.profile,name='profile'),
    path('profile-update/',views.profileUpdate,name='profileUpdate'),


    #login
    path('', views.LOGIN,name='login'),
    path('doLogin/',views.doLogin,name='doLogin'),
    path('doLogout/',views.doLogOut,name='doLogout'),
    #hod
    path('hod/home/',HOD_views.hodPanel,name='HODhome'),
    path('hod/student/add-student/',HOD_views.addStudent,name='addStudent'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
