from django.db import models

class Question(models.Model):
    question = models.CharField(null=False)
    text = models.TextField()

    def __str__(self):
        return self.text


class Answer(models.Model):
    answer = models.CharField(null=False)
    text = models.TextField()

    def __str__(self):
        return self.text

class QuestionRelate(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='related_question')
    answer_id = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='related_answer')
    next_question = models.ForeignKey(Question, related_name='next_question', on_delete=models.CASCADE)

    def __str__(self):
        return f"Question: {self.question_id.text}, Answer: {self.answer_id.text}, Next Question: {self.next_question.text}"

