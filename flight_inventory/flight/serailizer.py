from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'phone_number', 'first_name', 'password', 'is_superuser', 'is_staff')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        print(f"Validated Data: {validated_data}")
        password = self.validated_data.pop('password', None)
        print(f"Password : {password}")
        print(f"Validated data: {self.Meta.model(**validated_data)}")
        instance = self.Meta.model(**validated_data)
        print(f"Instance : {instance.password} | {instance.username}")
        if password is not None:
            instance.set_password(password)
        print(f"Instance: {instance.password}")
        instance.save()
        print(instance.save())
        return instance
