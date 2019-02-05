from django.test import TestCase


class TestDefaults(TestCase):
    def test_default_attrs_with_default_values(self):
        from foreign_user.core import RemoteUser, DEFAULT_ATTRS
        user = RemoteUser()

        for attr in DEFAULT_ATTRS:
            self.assertTrue(hasattr(user, attr))
            self.assertIsNone(getattr(user,attr))
