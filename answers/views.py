from django.shortcuts import render
from .models import Answer
from .serializers import AnswerSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from questions.models import TriviaQuestion
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class UserAnswerAddAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        question_id = request.data.get('question_id')
        question = TriviaQuestion.objects.get(id = question_id)

        data = {
            'user': user.pk,
            'question': question.pk,
            'selected_answer': request.data.get('selected_answer')
        }
        answer_serializer = AnswerSerializer(data = data)
        if answer_serializer.is_valid():
            answer_serializer.save()
            return Response({"status": True, 'data': answer_serializer}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": False, 'data': {'msg': answer_serializer.errors}}, status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, request):
        user = request.user
        answers = Answer.objects.filters(user = user.pk)
        serializer = AnswerSerializer(answers, many = True)
        if serializer.is_valid():
            return Response({'status': True, 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'status': False, 'data': {'msg': serializer.errors}}, status=status.HTTP_400_BAD_REQUEST)
        
