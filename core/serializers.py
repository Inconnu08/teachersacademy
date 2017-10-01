from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, CharField, Serializer

from task.models import Task

User = get_user_model()


class LoginSerializer(Serializer):
    email = serializers.EmailField(required=False)
    phone = serializers.CharField(required=False)
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    def _validate_phone(self, phone, password):
        user = get_object_or_404(User, phone=phone)

        if user and user.check_password(password):
            return user

    def _validate_email(self, email, password):
        user = get_object_or_404(User, email__iexact=email)

        if user and user.check_password(password):
            return user

    def validate(self, attrs):
        email = attrs.get('email')
        phone = attrs.get('phone')
        password = attrs.get('password')

        if phone and password:
            user = self._validate_phone(phone, password)
        elif email and password:
            user = self._validate_email(email, password)
        else:
            msg = _('Must include either "phone" or "email" and "password".')
            raise ValidationError(msg)

        if not user:
            msg = _('Unable to log in with provided credentials.')
            raise ValidationError(msg)

        # Everything passed. That means password is accepted. So return the user
        attrs['user'] = user
        return attrs


class RegistrationSerializer(ModelSerializer):
    password = CharField(style={'input_type': 'password'}, write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):

        password = validated_data.pop('password', None)
        if password:
            instance.set_password(password)

        obj = self.update(instance, validated_data)
        return obj

    class Meta:
        model = User
        fields = ['phone', 'email', 'password']


class UserPublicSerializer(ModelSerializer):
    tasks = PrimaryKeyRelatedField(many=True, queryset=Task.objects.all())

    class Meta:
        model = User
        fields = ('get_full_name', 'phone', 'email', 'date_of_birth', 'tasks')


class UserLiteSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('get_full_name', 'email')

