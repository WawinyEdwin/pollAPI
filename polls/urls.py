from django.urls import path
# from .views import polls_list, polls_detail
from rest_framework.routers import DefaultRouter

from .apiviews import ChoiceList, CreateVote, LoginView, PollViewSet, UserCreate

router = DefaultRouter()
router.register('polls', PollViewSet, basename='polls')

urlpatterns = [
    path("polls/<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"),
    path("polls/<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name="create_vote"),
    path("users/", UserCreate.as_view(), name="user_create"),
    path("login/", LoginView.as_view(), name="login")
]

urlpatterns += router.urls