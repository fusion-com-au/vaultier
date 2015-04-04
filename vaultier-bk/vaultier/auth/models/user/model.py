from django.contrib.auth.models import AbstractBaseUser
from django.db.models.fields import CharField, BooleanField
from vaultier.base.utils.changes.changes import ChangesMixin
from vaultier.base.utils.lowercasefield.lowercasefield import LowerCaseCharField
from vaultier.auth.models.user.manager import UserManager


class User(ChangesMixin, AbstractBaseUser):

    nickname = CharField(max_length=255, blank=False, null=False)
    public_key = CharField(max_length=1024)
    email = LowerCaseCharField(max_length=255, unique=True)
    is_active = BooleanField(default=True)

    objects = UserManager()

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'

    class Meta:
        db_table = u'vaultier_user'
