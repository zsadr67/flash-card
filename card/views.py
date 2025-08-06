
#from django.core.serializers import serialize
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404 ,get_list_or_404
from card.models import FlashCard
from card.serializer import CreateFlashCardSerializer, UpdateFlashCardSerializer



class CreateFlashCardView(APIView):

    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = CreateFlashCardSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data , status=status.HTTP_201_CREATED)


class UpdateFlashCardView(APIView):

    permission_classes = (IsAuthenticated,)

    def put(self, request, pk):
        flash_card = get_object_or_404(FlashCard, pk=pk)
        serializer = UpdateFlashCardSerializer(flash_card, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data , status=status.HTTP_200_OK)

class DeleteFlashCardView(APIView):

    permission_classes = (IsAuthenticated,)

    def delete(self, request, pk):
        flash_card = get_object_or_404(FlashCard, pk=pk)
        flash_card.delete()
        return Response({'status': 'deleted'} , status=status.HTTP_204_NO_CONTENT)


class ListFlashCardsView(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request , user_id):
        flash_card = get_list_or_404(FlashCard, user__id=user_id)
        serializer = CreateFlashCardSerializer(flash_card, many=True)
        return Response(serializer.data)


