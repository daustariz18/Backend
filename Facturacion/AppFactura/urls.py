from django.urls import path
from AppFactura import views
from django.urls import include


urlpatterns = [
    path('clients/', views.ClientsList.as_view()),
    path('clients/create/', views.ClientsCreate.as_view()),
    path('clients/update/<int:pk>/', views.ClientUpdate.as_view()),
    path('clients/delete/<int:pk>/', views.ClientDelete.as_view()),
    path('product/', views.ProductList.as_view()),
    path('product/create/', views.ProductCreate.as_view()),
    path('product/update/<int:pk>/', views.ProductUpdate.as_view()),
    path('product/delete/<int:pk>/', views.ProductDelete.as_view()),
    path('bills/', views.BillsList.as_view()),
    path('bills/create/', views.BillsList.as_view()),
    path('bills/update/<int:pk>/', views.BillsList.as_view()),
    path('bills/delete/<int:pk>/', views.BillsList.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]
