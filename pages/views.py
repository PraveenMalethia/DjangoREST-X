from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import *
from .serializers import *

# Create your views here.


class Index(APIView):
    """
    Home Page Get View.
    """

    def get(self, request, format=None):
        return Response({"message": "Welcome to the API."})


class About(APIView):
    """
    About Page Get View.
    """

    def get(self, request, format=None):
        return Response({"message": "Welcome to the API About Page."})
