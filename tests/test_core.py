# python imports
from unittest import mock

# external imports
from django.test import TestCase

# internal imports
from foreign_user import core
from tests.assets.serializers import TestCustomAttrsSerializer


class TestDefaults(TestCase):
    def test_default_attrs_with_default_values(self):
        user = core.get_foreign_user()()
        for attr in core.DEFAULT_ATTRS:
            try:
                self.assertTrue(hasattr(user, attr))
                self.assertIsNone(getattr(user,attr))
            except Exception as e:
                import pdb; pdb.set_trace()

    @mock.patch('foreign_user.core.foreign_user_settings')
    def test_custom_attrs_with_default_values(self, mocked_settings):
        type(mocked_settings).USER_SERIALIZER = \
            mock.PropertyMock(return_value=TestCustomAttrsSerializer)

        user = core.get_foreign_user()()
        custom_attrs = ['guid', 'identity']
        for attr in custom_attrs:
            self.assertTrue(hasattr(user, attr))
            self.assertIsNone(getattr(user,attr))
