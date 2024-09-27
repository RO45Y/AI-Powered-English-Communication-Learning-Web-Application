"""
URL configuration for mytycs1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from chat import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.dashboard, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.Homepage, name='Homepage'),
    path('register/', views.registerpage, name='register'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutpage, name='logout'),
    path('grammar/', views.grammar_list, name='grammar_list'),
    path('writing/', views.writing_topics, name='writing_topics'),
    path('listening/', views.listening_topics, name='listening_topics'),
    path('speaking/',views.speaking_topics,name='speaking_topics'),
    path('course/', views.course, name='course'),
    path('resource/', views.resource, name='resource'),
    path('lesson/complete/<int:lesson_id>/<str:lesson_type>/', views.mark_lesson_complete, name='mark_lesson_complete'),
]

# Add media URL patterns
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
