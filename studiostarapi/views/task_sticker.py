"""View module for handling requests about song genres"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from studiostarapi.models import TaskSticker, Task, Sticker


class TaskStickerView(ViewSet):
    """Studio Star API task_sticker view"""
    
    def retrieve(self, request, pk):
      """Handle GET requests for a single task_sticker
      
      Returns:
          Response -- JSON serialized task_sticker
      """
      
      try:
          task_sticker = TaskSticker.objects.get(pk=pk)
          
          serializer = TaskStickerSerializer(task_sticker)
          return Response(serializer.data, status=status.HTTP_200_OK)
        
      except TaskSticker.DoesNotExist as ex:
          return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
        
    def list(self, request):
      """Handle GET requests to get all task_stickers
    
      Returns:
          Response -- JSON serialized list of all task_stickers
      """
    
      task_stickers = TaskSticker.objects.all()
      
      # filter to query task_stickers by task_id
      task_id = request.query_params.get('task_id', None)
      
      if task_id is not None:
        task_stickers = task_stickers.filter(task_id_id=task_id)
      
      serializer = TaskStickerSerializer(task_stickers, many=True)
      return Response(serializer.data)
  
    def create(self, request):
        """Handle POST operations for task_sticker
        
        Returns
            Response -- JSON serialized task_sticker instance
        """
        
        task_id = Task.objects.get(pk=request.data["taskId"])
        sticker_id = Sticker.objects.get(pk=request.data["stickerId"])
        
        task_sticker = TaskSticker.objects.create(
            task_id=task_id,
            sticker_id=sticker_id
        )
        serializer = TaskStickerSerializer(task_sticker)
        
        # update the associated task's current_stickers field 
        task_sticker.update_task_current_stickers()
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def destroy(self, request, pk):
        try:
            task_sticker = TaskSticker.objects.get(pk=pk)
            task_sticker.delete()
            
            # update the associated task's current_stickers field
            task_sticker.update_task_current_stickers()
            
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except TaskSticker.DoesNotExist:
            return Response({'message': 'TaskSticker not found'}, status=status.HTTP_404_NOT_FOUND)
      

class TaskStickerSerializer(serializers.ModelSerializer):
  """JSON serializer for task_stickers"""

  class Meta:
      model = TaskSticker
      fields = ('id', 'task_id', 'sticker_id')
      depth = 1
