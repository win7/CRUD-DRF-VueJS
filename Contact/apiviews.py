from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.shortcuts import get_object_or_404

from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
# from rest_framework_jwt.views import refresh_jwt_token

from .models import Friend
from .serializers import FriendSerializer

class FriendList(APIView):
	"""
	List all friends, or create a new friend.
	"""
	permission_classes = (IsAuthenticated,)
	authentication_classes = (JSONWebTokenAuthentication,)
 
	def get(self, request):
		friends = Friend.objects.all()[:20]
		serializer = FriendSerializer(friends, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer = FriendSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

	""" def delete(self, request, pk):
		friend = get_object_or_404(Friend, pk=pk)
		friend.delete()
		return Response(status=status.HTTP_204_NO_CONTENT) """

class FriendDetail(APIView):
	"""
	Retrieve, update or delete a friend instance.
	"""
	""" def get_object(self, pk):
		try:
			return User.objects.get(pk=pk)
		except User.DoesNotExist:
			raise Http404 """
	permission_classes = (IsAuthenticated,)
	authentication_classes = (JSONWebTokenAuthentication,)

	def get(self, request, pk):
		friend = get_object_or_404(Friend, pk=pk)
		serializer = FriendSerializer(friend)
		return Response(serializer.data)

	def put(self, request, pk):
		friend = get_object_or_404(Friend, pk=pk)
		serializer = FriendSerializer(friend, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk):
		friend = get_object_or_404(Friend, pk=pk)
		friend.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

"""
HTTP_200_OK
HTTP_201_CREATED
HTTP_204_NO_CONTENT
HTTP_400_BAD_REQUEST
HTTP_401_UNAUTHORIZED
HTTP_403_FORBIDDEN """