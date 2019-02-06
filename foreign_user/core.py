# python imports
import os
import importlib
import collections
# internal imports
from foreign_user.settings import foreign_user_settings

# default attrs used on foreign_user.serializers.DefaultSerializer
DEFAULT_ATTRS = [
    'id', 'username', 'first_name', 'last_name', 'email',
    'is_staff', 'is_active', 'is_superuser', 'date_joined',
    'last_login'
]

def get_attrs():
    # import foreign_user_settings here
    # to prevent from being instantiated
    # before get_attrs is called


    # return attrs from USER_SERIALIZER fields
    return foreign_user_settings.USER_SERIALIZER() \
    .get_fields().keys()

def get_foreign_user():
    # get attributes for ForeignUser object
    # from serializer defined in settings
    # deafults to foreign_user.serializers.DefaultSerializer
    attrs = get_attrs()

    # create/return ForeignUser as named tuple
    # with attrs from get_attrs
    return collections.namedtuple(
        'ForeignUser', attrs, defaults=[None for _ in attrs])
                              # note: defaults here will not override
                              # defaults declared in serializer field kwargs
                              # this merely sets a sane default should
                              # the value be missing
