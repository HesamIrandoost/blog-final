import pytest
from django.utils import timezone
from datetime import timedelta
from Accounts.models import Profile, User


@pytest.fixture
def user(db, django_user_model):
    return django_user_model.objects.create_user(
        email="test@example.com",
        username="testuser",
        password="securepass123",
    )


@pytest.fixture
def profile(db, user):
    return Profile.objects.create(
        user=user,
        first_name="John",
        last_name="Doe",
        bio="Test bio",
    )


def test_create_user(user):
    assert user.email == "test@example.com"
    assert user.is_active is True
    assert user.is_staff is False
    assert user.is_verified is False
    assert user.check_password("securepass123")


def test_create_superuser(db, django_user_model):
    admin = django_user_model.objects.create_superuser(
        email="admin@example.com",
        username="admin",
        password="adminpass",
    )
    assert admin.is_staff is True
    assert admin.is_superuser is True
    assert admin.is_verified is True


def test_user_str(user):
    assert str(user) == "test@example.com"


def test_user_email_unique(db, django_user_model, user):
    with pytest.raises(Exception):
        django_user_model.objects.create_user(
            email="test@example.com",
            username="otheruser",
            password="pass",
        )


def test_create_user_without_email(db, django_user_model):
    with pytest.raises(ValueError):
        django_user_model.objects.create_user(email="", password="pass")



