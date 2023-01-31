import sqlite3

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from wordpair.models import Word
from wordpair.serializers import WordSerializer
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Create your views here.
@api_view(['GET', 'POST'])
def word_list(request, format=None):
    if request.method == 'GET':
        words = Word.objects.all()
        serializer = WordSerializer(words, many=True)
        #embedded with words : [{...},{...}]
        data = {"words" : serializer.data}
        return Response(data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = WordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE', 'PUT'])
def word_detail(request, pk, format=None):

    word = get_word(pk=pk)
    if request.method == 'PUT':
        serializer = WordSerializer(word, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)           
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    elif request.method == 'DELETE':
        word.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'GET':
        serializer = WordSerializer(word)
        return Response(serializer.data, status=status.HTTP_200_OK)


def get_word(pk):
    try:
        word = Word.objects.get(pk=pk)
        return word
    except Word.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
