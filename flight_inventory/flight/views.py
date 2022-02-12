from rest_framework.views import APIView
from .models import User
from .serailizer import UserSerializer
from rest_framework import status
from rest_framework.response import Response


class Signup(APIView):

    def post(self, request):
        data = request.data
        serialized = UserSerializer(data=data)
        serialized.is_valid(raise_exception=True)
        serialized.save()
        return Response(
            {'status': True,
             'Welcome User': serialized.data['username']}, status=status.HTTP_201_CREATED)
