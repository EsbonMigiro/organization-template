from rest_framework import serializers
from .models import Userr
from django.contrib.auth.hashers import make_password


class UserRegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Userr
        fields = (
            'username',
            'password',
            'confirm_password',
            'first_name',
            'last_name',
            'email',
            'alternative_email',
            'registration_no',
            'phone_number',
            'year_of_study')

    def create(self, validated_data):
        confirm_password = validated_data.pop('confirm_password', None)
        password = validated_data.get('password')

        if password != confirm_password:
            raise serializers.ValidationError("Passwords do not match.")

        user = Userr.objects.create_user(**validated_data)
        return user

class UserProfileUpdateSerializer(serializers.ModelSerializer):
    is_member = serializers.ReadOnlyField()
    is_corporate_member = serializers.ReadOnlyField()

    class Meta:
        model = Userr
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'alternative_email',
            'registration_no',
            'phone_number',
            'year_of_study',
            'leadership_role',
            'linkedin',
            'profile_image',
            'is_member',
            'is_corporate_member',
            'bio')

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            validated_data['password'] = make_password(
                validated_data['password'])

        instance = super().update(instance, validated_data)
        return instance


class PasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    confirm_new_password = serializers.CharField(required=True)
