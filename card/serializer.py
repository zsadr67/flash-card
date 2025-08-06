from card.models import FlashCard

from rest_framework import serializers


class CreateFlashCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlashCard
        fields = '__all__'

class UpdateFlashCardSerializer(serializers.ModelSerializer):

    class Meta:
        model = FlashCard
        fields = ('question', 'answer')