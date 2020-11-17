from rest_framework.routers import DefaultRouter

from polls import views

router = DefaultRouter()
router.register(
    r'polls/(?P<poll_id>[^/.]+)/questions/(?P<question_id>[^/.]+)/possible_answers',
    views.QuestionPossibleAnswersView,
    basename=r'polls/(?P<poll_id>[^/.]+)/questions/(?P<question_id>[^/.]+)/possible_answers'
)
router.register(
    r'polls/(?P<poll_id>[^/.]+)/questions',
    views.PollQuestionsView,
    basename=r'polls/(?P<poll_id>[^/.]+)/questions'
)
router.register('polls', views.PollsView)
router.register('questions', views.QuestionsView)
router.register('possible_answers', views.PossibleAnswersView)

urlpatterns = router.urls
