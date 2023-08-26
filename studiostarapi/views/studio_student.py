"""View module for handling requests about events"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from studiostarapi.models import Studio, User, StudioStudent
from rest_framework.decorators import action


class StudioStudentView(ViewSet):
  """Studio Star StudioStudent View"""
  
  #get single studio_student
  def retrieve(self, request, pk):
    """Handle GET requests for single studio_student
    
    Returns:
      Response -- JSON serialized studio_student
    """
    
    try:
        studio_student = StudioStudent.objects.get(pk=pk)
        serializer = StudioStudentSerializer(studio_student)
        return Response(serializer.data)
    except StudioStudent.DoesNotExist as ex:
        return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
      
  # get all studio_students 
  def list(self, request):
    """Handle GET requests to get all studio_students
    
    Returns:
      Response -- JSON serialized list of studio_students
    """
    
    studio_students = StudioStudent.objects.all()   
    serializer = StudioStudentSerializer(studio_students, many=True)
    return Response(serializer.data)

class StudioStudentSerializer(serializers.ModelSerializer):
  """JSON serializer for studio_students"""
  
  class Meta:
      model = StudioStudent
      fields = ('id', 'student_id', 'studio_id')
      depth = 0
