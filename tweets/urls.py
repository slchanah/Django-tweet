from django.urls import path  # url()

from tweets.views import (
    tweet_action_view, tweet_detail_view, tweet_list_view,
    tweet_create_view, tweet_delete_view
)

urlpatterns = [
    path('', tweet_list_view),
    path('action/', tweet_action_view),
    path('create/', tweet_create_view),
    path('<int:tweet_id>/', tweet_detail_view),
    path('<int:tweet_id>/delete/', tweet_delete_view),
]
