from .models import Word
from rest_framework import serializers


class WordSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Word
        fields = ['id', 'first_word', 'second_word']
        read_only_fields = ['id']

    