from django.contrib.auth.models import Group
from rest_framework.generics import ListCreateAPIView

from .serializers import GroupSerializer


class GroupsListView(ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
