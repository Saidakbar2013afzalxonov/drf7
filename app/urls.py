from django.urls import path
from . import views

urlpatterns = [
    path("companies/", views.CompanyListAPIView.as_view(), name="company-list"),
    path("companies/create/", views.CompanyCreateAPIView.as_view(), name="company-create"),
    path("companies/<int:pk>/", views.CompanyRetrieveAPIView.as_view(), name="company-detail"),
    path("companies/<int:pk>/update/", views.CompanyUpdateAPIView.as_view(), name="company-update"),
    path("companies/<int:pk>/delete/", views.CompanyDestroyAPIView.as_view(), name="company-delete"),
    path("companies/list-create/", views.CompanyListCreateAPIView.as_view(), name="company-list-create"),
    path("companies/<int:pk>/retrieve-update/", views.CompanyRetrieveUpdateAPIView.as_view(), name="company-retrieve-update"),
    path("companies/<int:pk>/retrieve-destroy/", views.CompanyRetrieveDestroyAPIView.as_view(), name="company-retrieve-destroy"),
    path("companies/<int:pk>/retrieve-update-destroy/", views.CompanyRetrieveUpdateDestroyAPIView.as_view(), name="company-retrieve-update-destroy"),
]