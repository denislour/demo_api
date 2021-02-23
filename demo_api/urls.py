from django.contrib import admin
from django.urls import path, include

from rest_framework.authtoken.views import obtain_auth_token 

from core.views import TestView, PostView, PostViewDetail

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('', TestView.as_view(), name='test'),
    path('post/', PostView.as_view(), name='test'),
    path('post/<int:pk>', PostViewDetail.as_view()),
    path('api/token/', obtain_auth_token, name='obtain-token')
]
