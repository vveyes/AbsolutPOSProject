from django.shortcuts import render, redirect
from django.views import View
from .models import Question, Answer, QuestionRelate


class QuestionView(View):
    template_name = 'polls_app/questions.html'
    size_template = 'polls_app/size.html'
    selected_answers = []

    def get(self, request):
        first_question = Question.objects.first()
        answers = Answer.objects.filter(related_answer__question_id=first_question)
        if not self.selected_answers:
            self.selected_answers.append({
                'question': first_question.text,
            })
        return render(request, self.template_name, {'question': first_question, 'answers': answers})

    def post(self, request):
        answer_id = request.POST.get('answer_id')
        answer = Answer.objects.get(pk=answer_id)
        
        self.selected_answers.append({
            'answer': answer.text
            })
        
        next_question = self.get_next_question(answer_id)
        answers = Answer.objects.filter(related_answer__question_id=next_question)
        
        if next_question:
            if next_question.text == 'Укажите размеры помещения:':
                request.session['selected_answers'] = self.selected_answers
                return render(request, self.size_template, {'question': next_question})
            else:
                answers = Answer.objects.filter(related_answer__question_id=next_question)

                self.selected_answers.append({
                    'question': next_question.text,
                })
                
                
                return render(request, self.template_name, {'question': next_question, 'answers': answers})
        else:
            return redirect('results')

    def get_next_question(self, answer_id):
        next_question = QuestionRelate.objects.filter(
            answer_id=answer_id).first()
        if next_question:
            return next_question.next_question
        else:
            return None
        
        
class ResultsView(View):
    template_name = 'polls_app/results.html'

    def post(self, request):
        selected_answers = request.session.get('selected_answers')
        area_size = request.POST.get('area_size')
        seating_capacity = request.POST.get('seating_capacity')
        hall_area = request.POST.get('hall_area')
        kitchen_area = request.POST.get('kitchen_area')
        
        return render(request, self.template_name, {
            'area_size': area_size,
            'seating_capacity': seating_capacity,
            'hall_area': hall_area,
            'kitchen_area': kitchen_area,
            'selected_answers': selected_answers
        })