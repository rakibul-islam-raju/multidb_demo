from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *


class UserCrudAPI(APIView):
    def get(self, request, *args, **kwargs):
        queryset = User.objects.using('user_db').all().values()
        return Response({
            'users': queryset
        })

    def post(self, request, *args, **kwargs):
        username = request.data['username']
        password = request.data['password']
        email = request.data['email']
        print(password)
        new_user = User.objects.using('user_db').create(
            username=username,
            email=email,
        )
        new_user.set_password(password)
        new_user.save()

        return Response({
            'status': 'created',
        })
