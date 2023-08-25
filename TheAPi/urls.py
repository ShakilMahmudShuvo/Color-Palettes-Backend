from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PaletteViewSet, PaletteSearchView

router = DefaultRouter()
router.register(r"palettes", PaletteViewSet)

urlpatterns = [
    path("", include(router.urls)),
  path("palette-search/", PaletteSearchView.as_view(), name="palette-search"), 
]
