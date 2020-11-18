from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from polls import views

router = DefaultRouter()

questions_url = r'questions'
possible_answers_url = 'possible_answers'
poll_url = r"polls"

poll_question_url = rf"{poll_url}/(?P<poll_id>[^/.]+)/{questions_url}"
poll_question_answer_url = rf"{poll_question_url}/(?P<question_id>[^/.]+)/{possible_answers_url}"

router.register(poll_question_answer_url, views.QuestionPossibleAnswersView, basename=poll_question_answer_url)
router.register(poll_question_url, views.PollQuestionsView, basename=poll_question_url)
router.register(poll_url, views.PollsView)
router.register(questions_url, views.QuestionsView)
router.register(possible_answers_url, views.PossibleAnswersView)

urlpatterns = router.urls
urlpatterns.append(path('api-token-auth/', obtain_auth_token))
