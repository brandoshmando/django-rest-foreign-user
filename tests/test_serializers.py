# python imports
from datetime import datetime, timezone
# external imports
from django.test import TestCase
from rest_framework import serializers
#internal imports
from foreign_user.serializers import DefaultSerializer, ForeignUserSerializer


class TestDefaultSerializer(TestCase):

    def test_create_instance_and_validate_success(self):
        date = datetime.now(timezone.utc)
        good_data = {
            'id': 1,
            'username': 'username',
            'first_name': 'brando',
            'last_name': 'shmando',
            'email': 'brandoshmando@example.com',
            'is_staff': True,
            'is_active': True,
            'is_superuser': True,
            'date_joined': date
        }

        serializer = DefaultSerializer(data=good_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(dict(serializer.validated_data), good_data)

    def test_handle_invalid_response_default_logic(self):
        bad_data = {
            'id': 'nan',
            'first_name': 'a' * 31,
            'last_name': 'shmando',
            'email': 'brandoshmando@example.com',
            'date_joined': 'nad'
        }

        serializer = DefaultSerializer(data=bad_data)

        with self.assertRaises(serializers.ValidationError):
            serializer.is_valid(raise_exception=False) # passing false doesn't
                                                       # stop error being raised

    def test_stubbed_methods(self):
        good_data = {
            'id': 1,
            'username': 'username',
            'first_name': 'brando',
            'last_name': 'shmando',
            'email': 'brandoshmando@example.com',
            'is_staff': True,
            'is_active': True,
            'is_superuser': True,
            'date_joined': str(datetime.now())
        }

        serializer = DefaultSerializer(data=good_data)
        serializer.is_valid()

        # test .create() is disabled
        with self.assertRaises(NotImplementedError):
            serializer.create({})

        # test .create() is disabled
        with self.assertRaises(NotImplementedError):
            serializer.update(None, {})

        # test .save() is disabled
        with self.assertRaises(NotImplementedError):
            serializer.save()

        # test .instance property always
        # returns None
        self.assertIsNone(serializer.instance)

    def test_handle_invalid_response_custom_logic(self):
        class TestSerializer(ForeignUserSerializer):
            test = serializers.CharField(max_length=1)

            class Meta:
                fields = ('test',)

            def handle_invalid_response(self, og_exception):
                return False

        # test is_valid runs custom
        # handle_invalid_response logic
        serializer = TestSerializer(data={})
        self.assertFalse(serializer.is_valid())
