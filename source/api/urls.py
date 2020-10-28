from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuoteViewSet,  VoteCreateView

router = DefaultRouter()
router.register('quote', QuoteViewSet, basename='quote')


app_name = 'api'


urlpatterns = [
    path('', include(router.urls)),
    path('vote/', VoteCreateView.as_view()),
]
