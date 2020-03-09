from django.urls import path
from questionnaire import views
from .views import (
    QuestionnaireListView,
    QuestionnaireCreateView
)

urlpatterns = [
    path("",views.home,name="home"),
    path("about/",views.about,name="about"),
    path("listview/",QuestionnaireListView.as_view(),name="questionnaire-list"),
    path("createview/",QuestionnaireCreateView.as_view(),name="questionnaire-create"),

]
    