from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from studiostarapi.models import Sticker


class StickerView(ViewSet):
  """Studio Star API sticker view"""
  
  def retrieve(self, request, pk):
    """Handle GET requests for a single sticker
    
    Returns:
        Response -- JSON serialized sticker
    """
    try:
      sticker = Sticker.objects.get(pk=pk)
      
      serializer = StickerSerializer(sticker)
      return Response(serializer.data, status=status.HTTP_200_OK)
    
    except Sticker.DoesNotExist as ex:
        return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
      
  def list(self, request):
    """Handle GET requests to get all stickers
    
    Returns:
        Response -- JSON serialized list of all stickers
    """
    
    stickers = Sticker.objects.all()
      
    serializer = StickerSerializer(stickers, many=True)
    return Response(serializer.data)

class StickerSerializer(serializers.ModelSerializer):
  """JSON serializer for stickers"""
  
  class Meta:
      model = Sticker
      fields = ('id', 'unicode')
      depth = 1
