import os
import importlib
import collections
from foreign_user.settings import foreign_user_settings

# attrs to use when no custom serializer is provided
DEFAULT_ATTRS = [
    'username', 'first_name', 'last_name', 'email',
    'is_staff', 'is_active', 'is_superuser', 'date_joined',
    'last_login'
]

CUSTOM_ATTRS = []
if foreign_user_settings.USER_SERIALIZER:
    CUSTOM_ATTRS = getattr(foreign_user_settings.USER_SERIALIZER, 'fields', [])

ATTRS = CUSTOM_ATTRS or DEFAULT_ATTRS

RemoteUser = collections.namedtuple('RemoteUser', ATTRS, defaults=[None for _ in ATTRS])
