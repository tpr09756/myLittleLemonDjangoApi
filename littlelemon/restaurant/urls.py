#define URL route for index() view
from django.urls import path
from .views import index, MenuItemsView, SingleMenuItemView, BookingViewSet
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('', index, name='index'),
    path('menu/',MenuItemsView.as_view()),
    #path('booking/',BookingViewSet),
    path('menu/<int:pk>',SingleMenuItemView.as_view()),
    #path('booking/<int:pk>',SingleBookingView),
    path('api-token-auth/', obtain_auth_token),
]