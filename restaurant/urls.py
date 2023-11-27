#define URL route for index() view
import rest_framework.routers
from django.urls import path

from . import views





urlpatterns = [
    path('', views.index, name='home'),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
]
