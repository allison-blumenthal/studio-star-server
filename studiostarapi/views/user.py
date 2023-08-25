from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from studiostarapi.models import User


class UserView(ViewSet):
  """Studio Star API User View"""

  def list(self, request):
    """Handle GET requests for users
    
    Returns 
      Response -- JSON serialized list of users
    """
    
    # get all users 
    users = User.objects.all()
    
    # Establish the query parameter of uid and 
    # use the .get method to retrieve the object with matching 
    # uid value. If no user is found, an exception is raised.
    uid = request.query_params.get('uid')
    
    # if the uid exists, filter the list of users by the uid
    if uid:
        users = users.filter(uid=uid)
    
    # serialize any matching instances
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)
  
  
  def retrieve(self, request, pk):
    """Handle GET request for a single user
    
    Returns -- JSON serialized user object
    """
    
    try:
        user = User.objects.get(pk=pk)
        
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
      
    except User.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND) 
    
      

class UserSerializer(serializers.ModelSerializer):
      """JSON serializer for rare_users"""
      
      class Meta:
        model = User
        fields = ('id', 'uid', 'is_teacher', 'instrument', 'first_name', 'last_name', 'pronouns', 'birthdate', 'guardian_names', 'email',  'profile_image_url', 'enrolled')
        depth = 1
          
    
