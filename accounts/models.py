import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# from cryptography.hazmat.backends import default_backend
# from cryptography.hazmat.primitives import serialization, hashes
# from cryptography.hazmat.primitives.asymmetric import padding
from django.core.signing import Signer
from encrypted_model_fields.fields import EncryptedCharField, EncryptedDateField, EncryptedEmailField


# with open("E:\Grad Project\suffrage\sffrg\key.pem", "rb") as key_file:
#     private_key = serialization.load_pem_private_key(
#         key_file.read(),
#         password=None,
#         backend=default_backend()
#     )
#
# # Derives private key from public key
# public_key = private_key.public_key()
#
# pub = private_key.public_key().public_bytes(
#     encoding=serialization.Encoding.PEM,
#     format=serialization.PublicFormat.SubjectPublicKeyInfo
# )


# Defines how both users and superusers(admins) are handled
class MyAccountManager(BaseUserManager):
    # Defines what happens when a new user is created
    def create_user(self, first_name, last_name, email, username, zip_code, dob, password=None):
        # Raises flag if no email or username is present
        if not email:
            raise ValueError("Users must have a valid email address")
        if not username:
            raise ValueError("Users must have a valid username")
        # normalizes email to lowercase
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            zip_code=zip_code,
            dob=dob
        )

        # Sets and saves password
        user.set_password(password)
        user.save(using=self._db)
        return user

    # Creates superuser
    def create_superuser(self, first_name, last_name, email, username, zip_code, dob, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            zip_code=zip_code,
            dob=dob
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


signer = Signer()


# Custom User Model
class Account(AbstractBaseUser):
    # Makes unique id using uuid ver. 4 (may be switched to ver. 5)  a 32 bit alphanumeric key generated from a random 128-bit number
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    # email = EncryptedEmailField(verbose_name="email", max_length=60, unique=True)
    # Uses fernet encryption, which combines 128-bit AES encryption with SHA-256 hashing
    # first_name = models.CharField(max_length=20)
    first_name = EncryptedCharField(max_length=20)
    # last_name = models.CharField(max_length=20)
    last_name = EncryptedCharField(max_length=20)
    username = models.CharField(max_length=20, unique=True)
    # Charfield because zip codes can start with 0, Int doesn't support that
    # zip_code = models.CharField(max_length=5, blank=True, null=True)
    zip_code = EncryptedCharField(max_length=5, blank=True, null=True)
    # dob = models.DateField(verbose_name="date of birth", auto_now=False, auto_now_add=False)
    dob = EncryptedDateField(verbose_name="date of birth", auto_now=False, auto_now_add=False)

    # Required for AbstractBaseUser
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # Defines what is used for authentication and what is required
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username', 'zip_code', 'dob']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    # Only allows certain permissions if user is admin
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
