from django import forms
from .models import QuestionnaireResponse



class QuestionnaireForm(forms.ModelForm):
    class Meta:
        model = QuestionnaireResponse
        fields = ["name","gender","age","nationality","question_1","question_2","question_3","question_3_subquestion_1","question_3_subquestion_2","question_3_subquestion_3","question_3_subquestion_4"]
        widgets = {
            'question_3':forms.CheckboxSelectMultiple(),
            'question_3_subquestion_1':forms.RadioSelect(),
        }