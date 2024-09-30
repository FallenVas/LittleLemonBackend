from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.MenuItemView.as_view() , name='menu'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view() , name='menu_item') ,
    path('message/', views.msg),
    path('api-token-auth/', obtain_auth_token)
]