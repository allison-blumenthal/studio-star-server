"""View module for handling requests about song genres"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from studiostarapi.models import TeacherStudent, User


class TeacherStudentView(ViewSet):
    """Studio Star API teacher_student view"""
    
    def retrieve(self, request, pk):
      """Handle GET requests for a single teacher_student
      
      Returns:
          Response -- JSON serialized teacher_student
      """
      
      try:
          teacher_student = TeacherStudent.objects.get(pk=pk)
          
          serializer = TeacherStudentSerializer(teacher_student)
          return Response(serializer.data, status=status.HTTP_200_OK)
        
      except TeacherStudent.DoesNotExist as ex:
          return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
        
    def list(self, request):
      """Handle GET requests to get all teacher_students
    
      Returns:
          Response -- JSON serialized list of all teacher_students
      """
    
      teacher_students = TeacherStudent.objects.all()
      
      # filter to query teacher_students by teacher_id
      teacher_id = request.query_params.get('teacher_id', None)
      # filter to query by student_id
      student_id = request.query_params.get('student_id', None)
      
      if teacher_id is not None:
        teacher_students = teacher_students.filter(teacher_id_id=teacher_id)
        
      if student_id is not None:
        teacher_students = teacher_students.filter(student_id_id=student_id)
      
      serializer = TeacherStudentSerializer(teacher_students, many=True)
      return Response(serializer.data)
  
    def create(self, request):
        """Handle POST operations for teacher_student
        
        Returns
            Response -- JSON serialized teacher_student instance
        """
        
        teacher_id = User.objects.get(pk=request.data["teacherId"])
        student_id = User.objects.get(pk=request.data["studentId"])
        
        teacher_student = TeacherStudent.objects.create(
            teacher_id=teacher_id,
            student_id=student_id,
        )
        serializer = TeacherStudentSerializer(teacher_student)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def destroy(self, request, pk):
      teacher_student = TeacherStudent.objects.get(pk=pk)
      teacher_student.delete()
      return Response(None, status=status.HTTP_204_NO_CONTENT)
      

class TeacherStudentSerializer(serializers.ModelSerializer):
  """JSON serializer for teacher_students"""

  class Meta:
      model = TeacherStudent
      fields = ('id', 'teacher_id', 'student_id')
      depth = 2
