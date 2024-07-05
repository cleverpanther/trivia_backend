# In your_app/models.py
from django.db import models

class TriviaQuestion(models.Model):
    question_text = models.CharField(max_length=255)
    possible_answers_A = models.CharField(max_length=255)
    possible_answers_B = models.CharField(max_length=255)
    possible_answers_C = models.CharField(max_length=255)
    possible_answers_D = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=20)  # Assuming A, B, C, or D
    category = models.CharField(max_length=100, default="general")
    explanation = models.CharField(max_length=255)
    difficulty_level = models.CharField(max_length=50, default="easy")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'questions_tbl'

    def __str__(self):
        return self.question_text