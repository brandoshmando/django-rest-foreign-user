from django.conf import settings
from rest_framework.settings import APISettings


FOREIGN_USER_SETTINGS = getattr(settings, 'FOREIGN_USER_SETTINGS', {})

DEFAULTS = {
    'USER_SERIALIZER': None
}

IMPORT_STRINGS = {
    'USER_SERIALIZER'
}

foreign_user_settings = APISettings(FOREIGN_USER_SETTINGS, DEFAULTS, IMPORT_STRINGS)
