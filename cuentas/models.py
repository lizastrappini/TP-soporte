from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.

class CustomUserManager(BaseUserManager):

    def _create_user(self, username, email, password, **extra_fields):

        if not username:
            raise ValueError("Username must be provided")
        if not email:
            raise ValueError("Email must be provided")
        if not password:
            raise ValueError("Password must be provided")

        user = self.model(
            username = username,
            email = self.normalize_email(email),
            **extra_fields,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password, **extra_fields):

        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):

        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self._create_user(username, email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):

    required_error_text = "Este campo debe ser rellenado"

    username = models.CharField(
        "username",
        max_length=150,
        unique=True,
        error_messages={
            "unique": "Ese nombre de usuario ya existe.",
        },
    )

    email = models.EmailField(
        unique=True, 
        max_length=254, 
        error_messages={"required": required_error_text},
    )

    nombre = models.CharField(
        max_length=254,
        blank=True,
    )

    apellido = models.CharField(
        max_length=254, 
        blank=True,
    )

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = [
        "email",
    ]
