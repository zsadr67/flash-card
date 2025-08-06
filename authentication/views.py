
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from authentication.serializer import CreateUserProfileSerializer

class CreateUserView(APIView):

    def post(self, request):
        serializer = CreateUserProfileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        user_data = User(
            username=data['username'],
            email=data['email'],
        )

        user_data.set_password(data['password'])
        user_data.save()

        return Response(serializer.data)