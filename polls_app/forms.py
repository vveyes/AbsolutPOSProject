from django import forms
from .models import QuestionRelate, Answer

class QuestionRelateForm(forms.ModelForm):
    class Meta:
        model = QuestionRelate
        fields = ['question_id', 'answer_id', 'next_question']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        used_answers = QuestionRelate.objects.values_list('answer_id', flat=True)
        self.fields['answer_id'].queryset = Answer.objects.exclude(id__in=used_answers)
