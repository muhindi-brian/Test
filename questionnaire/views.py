from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    FormView,
)
from .models import QuestionnaireResponse
from .forms import QuestionnaireForm

def home(request):
    return render(request, "questionnaire/home.html")

def about(request):
    return render(request, "questionnaire/about.html")


class QuestionnaireListView(ListView):
    model = QuestionnaireResponse
    context_object_name = "questionnaire"
    template_name = "questionnaire/list_view.html"
    ordering = ["-date_published"]


class QuestionnaireCreateView(CreateView):
    form_class = QuestionnaireForm
    template_name = "questionnaire/questionnaireresponse_form.html"
    success_url = "/listview/"


