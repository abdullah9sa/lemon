from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializer import *
from rest_framework.generics import ListCreateAPIView,RetrieveAPIView
# Create your views here.
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

def indexPage(request):
    return render(request, 'index.html', {})


class bookingView(ListCreateAPIView):
    queryset = booking.objects.all()
    serializer_class = bookingSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class menuView(ListCreateAPIView):
    queryset = menu.objects.all()
    serializer_class = menuSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class SingleMenuItemView(RetrieveAPIView):
    queryset = menu.objects.all()
    serializer_class = menuSerializer
    lookup_field = 'pk'
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
#TestCase class

