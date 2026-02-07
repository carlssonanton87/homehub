from django.urls import path
from . import views
from .views import DocumentDeleteView

app_name = "documents"

urlpatterns = [
    path("", views.document_list, name="list"),
    path("create/", views.document_create, name="create"),
    path("<int:pk>/", views.document_detail, name="detail"),
    path("<int:pk>/edit/", views.document_update, name="update"),
    path("<int:pk>/delete/", DocumentDeleteView.as_view(), name="delete"),
]
