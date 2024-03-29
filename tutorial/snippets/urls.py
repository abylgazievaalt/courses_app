from django.urls import path, include
from rest_framework import routers
from snippets import views
from rest_framework.schemas import get_schema_view

# Create a router and register our viewsets with it.
router = routers.DefaultRouter()
router.register(r'snippets', views.CourseView)
router.register(r'categories', views.CategoriesView)

schema_view = get_schema_view(title='Pastebin API')

# The API URLs are now determined automatically by the router.
urlpatterns = [
	path('schema/', schema_view),
    path('', include(router.urls)),
]