from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from studiostarapi.models import Task, Assignment


class TaskView(ViewSet):
  """Studio Star API task view"""
  
  def retrieve(self, request, pk):
    """Handle GET requests for a single task
    
    Returns:
        Response -- JSON serialized task
    """
    try:
      task = Task.objects.get(pk=pk)
      
      serializer = TaskSerializer(task)
      return Response(serializer.data, status=status.HTTP_200_OK)
    
    except Task.DoesNotExist as ex:
        return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
      
  def list(self, request):
    """Handle GET requests to get all tasks
    
    Returns:
        Response -- JSON serialized list of all tasks
    """
    
    tasks = Task.objects.all()
    
    # filter to query by assignment_id
    assignment_id = request.query_params.get('assignment_id', None)
    
    if assignment_id is not None: 
      tasks = tasks.filter(assignment_id_id=assignment_id)
      
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)
  
  def create(self, request):
    """Handle POST operations for task
    
    Returns:
        Response -- JSON serialized task instance
    """
    
    assignment_id = Assignment.objects.get(pk=request.data["assignmentId"])
    
    task = Task.objects.create(
      assignment_id=assignment_id,
      title=request.data["title"],
      description=request.data["description"],
      sticker_goal=request.data["stickerGoal"],
      current_stickers=request.data["currentStickers"],
      is_completed=request.data["isCompleted"]
    )
    serializer = TaskSerializer(task)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
    
  def update(self, request, pk):
    """Handle PUT requests for an task
    
    Returns:
        Response -- Empty body with 204 status code
    """
    try:
      task = Task.objects.get(pk=pk)
      
      assignment_id = Assignment.objects.get(pk=request.data["assignmentId"])
      task.assignment_id=assignment_id
      
      task.title=request.data["title"]
      task.description=request.data["description"]
      task.sticker_goal=request.data["stickerGoal"]
      task.current_stickers=request.data["currentStickers"]
      task.is_completed = task.current_stickers >= task.sticker_goal
      
      task.save()
      
      return Response(None, status=status.HTTP_204_NO_CONTENT)
    except Task.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
  
  def destroy(self, request, pk):
      task = Task.objects.get(pk=pk)
      task.delete()
      return Response(None, status=status.HTTP_204_NO_CONTENT)


class TaskSerializer(serializers.ModelSerializer):
  """JSON serializer for tasks"""
  
  class Meta:
      model = Task
      fields = ('id', 'assignment_id', 'title', 'description', 'sticker_goal', 'current_stickers', 'is_completed')
      depth = 1
