from rest_framework import serializers
from .models import Account

from django.contrib.auth.hashers import make_password

"""
Serializers convert complex django objects (Models and Querysets) into simpler python data types (lists and dicts)
lists and dicts can futher be converted into JSON or other formats, which are used to data transfer b/w client and API
deserialization is the opposite process
"""

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'username', 'password', 'displayname', 'bio']
        extra_kwargs = {
            'password': {'write_only': True} # password is not included in serializer response
        }

    """
    we need to overwrite the update and create methods to hash the password
    """

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data=validated_data)
    
    def update(self, instance, validated_data):
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data['password'])
        return super().update(instance, validated_data)
