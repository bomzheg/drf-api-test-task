from rest_framework.routers import DefaultRouter

from polls import views

app_name = 'polls'

router = DefaultRouter()
router.register('polls', views.PollsView)
router.register('questions', views.QuestionsView)
router.register('possible_answers', views.PossibleAnswersView)

urlpatterns = router.urls
