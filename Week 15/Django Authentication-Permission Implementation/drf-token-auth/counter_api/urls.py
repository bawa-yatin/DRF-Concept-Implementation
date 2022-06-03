from django.urls import path
from .views import *
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', index),
    path('api/', count_word),
    path('api/<int:pk>/', count_word_each),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
