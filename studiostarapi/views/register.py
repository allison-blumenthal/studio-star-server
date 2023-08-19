from studiostarapi.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import date

# api_view decorator with 'POST' passed as an argument
# indicating that this view function should handle POST requests.
# By using this decorator, we make sure the assocaited view function
# will only be called when a POST request is made to the corresponding 
# endpoint. 
@api_view(['POST'])
def check_user(request):
    """Checks to see if a User has registered in the app yet
    
    Method arguments:
      request -- The full HTTP request object
    """
    
    uid = request.data['uid']
    
    # Use the built-in authentication method to verify
    # authentication returns the user object or None if no user.
    # The .first method is used to retrieve the first object that
    # matches the filter criteria, or "none" if it doesn't exist.
    # Since uid is a unique identifier, 
    # we can call the .first method on the queryset and ensure that only 
    # a single user object is retrieved, even if there are multiple 
    # users with the same uid.
    user = User.objects.filter(uid=uid).first()
    
    # If authentication was successful, respond with their token
    if user is not None:
      data = {
        'id': user.id,
        'uid': user.uid,
        'is_teacher': user.is_teacher,
        'instrument': user.instrument,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'pronouns': user.pronouns,
        'birthdate': user.birthdate,
        'guardian_names': user.guardian_names,
        'email': user.email,
        'profile_image_url': user.profile_image_url,
      }
      return Response(data)
    else: 
      # Bad login details were provided, so we can't log the user in
      data = {'valid': False}
      return Response(data)
  
@api_view(['POST'])
def register_user(request):
  """Handles the creation of a new registered user in the app
  
  Method arguments:
    request -- The full HTTP request object
  """
  
  #Now save the user info in the the bangazonapi_user table
  user = User.objects.create(
    uid = request.data['uid'],
    is_teacher = request.data['isTeacher'],
    instrument = request.data['instrument'],
    first_name = request.data['firstName'],
    last_name = request.data['lastName'],
    pronouns = request.data['pronouns'],
    birthdate = request.data['birthdate'],
    guardian_names = request.data['guardianNames'],
    email = request.data['email'],
    profile_image_url = request.data['profileImageUrl']
  )
  
  # Return the user info to the client
  data = {
      'id': user.id,
      'uid': user.uid,
      'is_teacher': user.is_teacher,
      'instrument': user.instrument,
      'first_name': user.first_name,
      'last_name': user.last_name,
      'pronouns': user.pronouns,
      'birthdate': user.birthdate,
      'guardian_names': user.guardian_names,
      'email': user.email,
      'profile_image_url': user.profile_image_url,
  }
  
  return Response(data)
