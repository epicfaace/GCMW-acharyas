# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets
from .serializers import AcharyaSerializer, CentreSerializer
from .models import Acharya, Centre
from django.views import View
import urllib2
import json

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

class IndexView(View):
    template_name = "index.html"
    def get(self, request, *args, **kwargs):
        url = 'http://localhost:49573/wp-json/gcmw/v1/options'
        serialized_data = urllib2.urlopen(url).read()
        headerData = json.loads(serialized_data)
        context = {'header': headerData}
        return render(request, self.template_name, context)