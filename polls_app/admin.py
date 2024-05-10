from django import forms
from django.contrib import admin
from django.db import models
from .models import Question, Answer, QuestionRelate
from .forms import QuestionRelateForm


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'text')

    list_display_links = ('question',)
    list_editable = ('text',)
    ordering = ('question',)

    formfield_overrides = {
        models.TextField: {'widget': forms.TextInput(attrs={'size': '80'})},
    }


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('answer', 'text')
    list_display_links = ('answer',)
    list_editable = ('text',)
    ordering = ('answer',)

    formfield_overrides = {
        models.TextField: {'widget': forms.TextInput(attrs={'size': '20'})},
    }


@admin.register(QuestionRelate)
class QuestionRelateAdmin(admin.ModelAdmin):
    list_display = ('question_id','answer_id','next_question')
    form = QuestionRelateForm

    