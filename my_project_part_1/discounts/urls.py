# TODO настраиваем urls здесь
from django.urls import path

from discounts import views

urlpatterns = [
    path('', views.DiscountListView.as_view()),
    path('<int:pk>/', views.DiscountDetailView.as_view()),
]
