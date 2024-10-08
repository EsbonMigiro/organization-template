from rest_framework import generics, viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Userr
from .serializers import (
    UserRegistrationSerializer,
    UserProfileUpdateSerializer,
    PasswordChangeSerializer,

)

from django.shortcuts import render

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.parsers import (
    MultiPartParser, FormParser, FileUploadParser
)
from django.db.models import Case, Value, When, IntegerField


class UserLoginView(TokenObtainPairView):
    pass




class UserRegistrationView(generics.CreateAPIView):
    queryset = Userr.objects.all()
    serializer_class = UserRegistrationSerializer
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    



class UserProfileView(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

    def retrieve(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = UserProfileUpdateSerializer(user)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = UserProfileUpdateSerializer(
            user, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)

    def change_password(self, request):
        user = self.get_object()
        serializer = PasswordChangeSerializer(data=request.data)

        if serializer.is_valid():
            old_password = serializer.validated_data.get('old_password')
            new_password = serializer.validated_data.get('new_password')
            confirm_new_password = serializer.validated_data.get(
                'confirm_new_password')

            if not user.check_password(old_password):
                return Response(
                    {'detail': 'Old password is incorrect.'},
                    status=status.HTTP_400_BAD_REQUEST)

            if new_password != confirm_new_password:
                return Response(
                    {'detail': 'New passwords do not match.'},
                    status=status.HTTP_400_BAD_REQUEST)

            user.set_password(new_password)
            user.save()
            return Response(
                {'detail': 'Password successfully changed.'},
                status=status.HTTP_200_OK)
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)

