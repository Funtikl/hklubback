from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from backend.serializers import UserSerializer, InneedPeopleSerializer
from backend.models import Users


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Users.objects.all()
    serializer_class = UserSerializer
     

class InneedPeopleViewSet(viewsets.ModelViewSet):

    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = ''
    serializer_class = InneedPeopleSerializer