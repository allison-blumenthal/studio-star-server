from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from studiostarapi.models import Studio, User


class StudioView(ViewSet):
  """Studio Star API studio view"""
  
  def retrieve(self, request, pk):
    """Handle GET requests for a single studio
    
    Returns:
        Response -- JSON serialized studio
    """
    try:
      studio = Studio.objects.get(pk=pk)
      
      serializer = StudioSerializer(studio)
      return Response(serializer.data, status=status.HTTP_200_OK)
    
    except Studio.DoesNotExist as ex:
        return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
      
  def list(self, request):
    """Handle GET requests to get all studios
    
    Returns:
        Response -- JSON serialized list of all studios
    """
    
    studios = Studio.objects.all()
    
    # filter to query by teacher_id
    teacher_id = request.query_params.get('teacher_id', None)
    
    if teacher_id is not None: 
      studios = studios.filter(teacher_id_id=teacher_id)
      
    serializer = StudioSerializer(studios, many=True)
    return Response(serializer.data)
  
  def create(self, request):
    """Handle POST operations for studio
    
    Returns:
        Response -- JSON serialized studio instance
    """
    
    teacher_id = User.objects.get(pk=request.data["teacherId"])
    
    studio = Studio.objects.create(
      teacher_id=teacher_id,
      name=request.data["name"]
    )
    serializer = StudioSerializer(studio)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


class StudioSerializer(serializers.ModelSerializer):
  """JSON serializer for studios"""
  
  class Meta:
      model = Studio
      fields = ('id', 'teacher_id', 'name')
      depth = 1
