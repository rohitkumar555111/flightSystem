
from django.contrib import admin
from django.urls import path, include
from flightApp import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('flights', views.FlightViewSet)
router.register('passengers', views.PasserngerViewSet)
router.register('reservation', views.ReservationViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('searchFlights/', views.searchFlights),
    path('save_reservation/', views.save_reservation),
]
