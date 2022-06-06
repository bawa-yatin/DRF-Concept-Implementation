from django.urls import path, include
from rest_framework import routers
from .views import ArticleView

router = routers.DefaultRouter()
router.register(r'item', ArticleView)

urlpatterns = [
    path('', include(router.urls))
]