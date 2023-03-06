#define URL route for index() view
from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.indexPage, name='home'),
    path('api/menu/', menuView.as_view()),
    path('api/menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('api/booking/', bookingView.as_view()),
]
