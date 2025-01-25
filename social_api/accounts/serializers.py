from rest_framework import serializers
from .models import Account

"""
Serializers convert complex django objects (Models and Querysets) into simpler python data types (lists and dicts)
lists and dicts can futher be converted into JSON or other formats, which are used to data transfer b/w client and API
deserialization is the opposite process
"""

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'username', 'password', 'displayname', 'bio']