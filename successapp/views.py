from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import Comment
from .serializer import CommentSerializers
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action

# Create your views here.

def home(request):
    return HttpResponse('hello world')

class CommentSerialze(ModelViewSet):
    queryset= Comment.objects.all()
    serializer_class= CommentSerializers
    permission_classes= [AllowAny]

    @action(detail= False, methods=(['GET']))
    def recent(self, request):
        recent_comment= Comment.objects.all()[:3]
        serializer= CommentSerializers(recent_comment, many= True)
        return Response(serializer.data)