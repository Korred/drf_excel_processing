from django.urls import path, include
from rest_framework.routers import DefaultRouter
from excel_api import views


app_name = ''

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r"excel_documents", views.ExcelDocumentViewSet)
urlpatterns = [
    path("", include(router.urls)),   
]
