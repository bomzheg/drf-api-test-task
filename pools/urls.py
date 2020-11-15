from rest_framework.routers import DefaultRouter

from . import views

app_name = 'pools'

router = DefaultRouter()
router.register('pools', views.PoolsView)
router.register('question', views.QuestionsView)
router.register('answer', views.AnswersView)

urlpatterns = router.urls
