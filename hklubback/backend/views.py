from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from hklubback.backend.serializers import UserSerializer, InneedPeopleSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class InneedPeopleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Inneed_people.objects.all()
    serializer_class = InneedPeopleSerializer