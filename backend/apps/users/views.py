from rest_framework import views
from rest_framework.response import Response

from .serializers import UserSerializer


class UserAPIView(views.APIView):
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data)
