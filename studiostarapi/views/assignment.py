from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from studiostarapi.models import Assignment, User


class AssignmentView(ViewSet):
  """Studio Star API assignment view"""
  
  def retrieve(self, request, pk):
    """Handle GET requests for a single assignment
    
    Returns:
        Response -- JSON serialized assignment
    """
    try:
      assignment = Assignment.objects.get(pk=pk)
      
      serializer = AssignmentSerializer(assignment)
      return Response(serializer.data, status=status.HTTP_200_OK)
    
    except Assignment.DoesNotExist as ex:
        return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
      
  def list(self, request):
    """Handle GET requests to get all assignments
    
    Returns:
        Response -- JSON serialized list of all assignments
    """
    
    assignments = Assignment.objects.all()
    
    # filter to query by student_id
    student_id = request.query_params.get('student_id', None)
    
    if student_id is not None: 
      assignments = assignments.filter(student_id_id=student_id)
      
      # filter to query by task_id
    task_id = request.query_params.get('task_id', None)
    
    if task_id is not None:
      assignments = Assignment.objects.filter(task__id=task_id)
    
      
    serializer = AssignmentSerializer(assignments, many=True)
    return Response(serializer.data)
  
  def create(self, request):
    """Handle POST operations for assignment
    
    Returns:
        Response -- JSON serialized assignment instance
    """
    
    student_id = User.objects.get(pk=request.data["studentId"])
    
    assignment = Assignment.objects.create(
      student_id=student_id,
      date=request.data["date"]
    )
    serializer = AssignmentSerializer(assignment)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
    
  def update(self, request, pk):
    """Handle PUT requests for an assignment
    
    Returns:
        Response -- Empty body with 204 status code
    """
    
    assignment = Assignment.objects.get(pk=pk)
    
    student_id=User.objects.get(pk=request.data["studentId"])
    assignment.student_id=student_id
    
    assignment.date=request.data["date"]
  
    assignment.save()
    
    return Response(None, status=status.HTTP_204_NO_CONTENT)
  
  def destroy(self, request, pk):
      assignment = Assignment.objects.get(pk=pk)
      assignment.delete()
      return Response(None, status=status.HTTP_204_NO_CONTENT)


class AssignmentSerializer(serializers.ModelSerializer):
  """JSON serializer for assignments"""
  
  class Meta:
      model = Assignment
      fields = ('id', 'student_id', 'date')
      depth = 1
