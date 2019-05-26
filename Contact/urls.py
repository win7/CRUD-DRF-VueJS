from django.urls import path
from .apiviews import FriendList, FriendDetail
from Contact import views

urlpatterns = [
    path("friends/", FriendList.as_view(), name="friends_list"),
    path("friend/<int:pk>/", FriendDetail.as_view(), name="friends_detail"),
]