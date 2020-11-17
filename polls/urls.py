from rest_framework.routers import DefaultRouter

from polls import views

app_name = 'polls'

router = DefaultRouter()
router.register('polls', views.PollsView)
router.register('questions', views.QuestionsView)
router.register('answers', views.AnswersView)

urlpatterns = router.urls
