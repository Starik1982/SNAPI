from django.contrib.auth import get_user_model



from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView
)

from rest_framework.permissions import (
    AllowAny
)

from loginsys.api.serializers import (
    UserCreateSerializer,
  
)
User = get_user_model()

class UserCreateAPI(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()


