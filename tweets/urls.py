from django.urls import path, include  # url()
from rest_framework.routers import DefaultRouter

from tweets.views import (
    tweet_action_view, tweet_detail_view, tweet_list_view,
    tweet_create_view, tweet_delete_view, TweetViewSet
)

router = DefaultRouter()
router.register('', TweetViewSet)

urlpatterns = [
    # path('', tweet_list_view),
    # path('action/', tweet_action_view),
    # path('create/', tweet_create_view),
    # path('<int:tweet_id>/', tweet_detail_view),
    # path('<int:tweet_id>/delete/', tweet_delete_view),
    path('', include(router.urls))
]
