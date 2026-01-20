from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import User
from laboratories.models import Laboratory

class UserSerializer(serializers.ModelSerializer):
    laboratoryId = serializers.PrimaryKeyRelatedField(
        source='laboratory',
        queryset=Laboratory.objects.all(),
        required=False,
        allow_null=True
    )

    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = [
            'id',
            'name',
            'email',
            'password',
            'role',
            'id_number',
            'address',
            'laboratoryId',
            'job_role',
            'phone',
            'gender',
            'bio',
            'postal_address',
            'town',
            'country',
            'created_at',
            'updated_at',
        ]

    def create(self, validated_data):
        password = validated_data.pop('password')
        validated_data['password'] = make_password(password)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            instance.password = make_password(validated_data.pop('password'))
        return super().update(instance, validated_data)
