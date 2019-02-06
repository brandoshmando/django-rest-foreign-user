# external imports
from rest_framework import serializers
# internal imports
from foreign_user.serializers import ForeignUserSerializer

class TestCustomAttrsSerializer(ForeignUserSerializer):
    guid = serializers.CharField()
    identity = serializers.IntegerField()

    class Meta:
        fields = ('guid', 'identity')
