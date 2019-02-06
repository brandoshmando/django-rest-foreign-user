# external imports
from django.contrib.auth.models import User
from django.db import models
from rest_framework import serializers
from rest_framework.utils.field_mapping import ClassLookupDict, get_field_kwargs
# internal imports
from foreign_user.core import DEFAULT_ATTRS




class ForeignUserSerializer(serializers.Serializer):

    def is_valid(self, *args, **kwargs):

        try:
            is_valid = super(ForeignUserSerializer, self)\
                            .is_valid(raise_exception=True)
        except serializers.ValidationError as e:
            return self.handle_invalid_response(e)

        return is_valid

    def handle_invalid_response(self, og_exception):
        # default behavior is to re-raise the
        # original exception when response is invalid
        raise og_exception


class DefaultSerializer(serializers.ModelSerializer,
                             ForeignUserSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = User
        fields = DEFAULT_ATTRS

    def __init__(self, *args, **kwargs):
        super(DefaultSerializer, self).__init__(*args, **kwargs)
        self.instance = None # ensure instance is always None

    def create(self, *args, **kwargs):
        raise NotImplementedError('Cannot use create method with ForeignUser instance')

    def update(self, *args, **kwargs):
        raise NotImplementedError('Cannot use update method with ForeignUser instance')

    def save(self, *args, **kwargs):
        raise NotImplementedError('Cannot use save method with ForeignUser instance')
