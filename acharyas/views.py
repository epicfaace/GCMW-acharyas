# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets
from .serializers import AcharyaSerializer, CentreSerializer
from .models import Acharya, Centre

class AcharyaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows acharya to be viewed or edited.
    """
    queryset = Acharya.objects.all().order_by('-name')
    serializer_class = AcharyaSerializer

class AcharyaDetailViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows acharya to be viewed or edited.
    """
    queryset = Acharya.objects.all().order_by('-name')
    serializer_class = AcharyaSerializer

class CentreViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Centre.objects.all()
    serializer_class = CentreSerializer