import pytest
import pytest_django
from django.core import mail
from django.urls import reverse
from mixer.backend.django import mixer
from django.contrib.auth.models import User
from .models import Password
from .forms import SharePassword

@pytest.fixture
def password():
    return mixer.blend(Password)


@pytest.fixture
def user():
    return mixer.blend(User)


@pytest.fixture
def client():
    from django.test import Client
    client = Client()
    return client


@pytest.mark.django_db
def test_password_share_get(client, password, user):
    client.force_login(user)
    response = client.get(reverse('password:share_password', kwargs={'slug': password.slug}))
    assert response.status_code == 200
    assert 'password/share_password.html' in [template.name for template in response.templates]


@pytest.mark.django_db
def test_password_share_post(client, password, user, settings):
    client.force_login(user)
    form_data = {
        'email_to': 'atomsis01@mail.ru',
        'email_from': 'amadeusfaust98@gmail.com',
        'name': 'Test User',
        'anonymity': 'anonymous',
        'comments': 'Test comments'
    }
    print("Form data:", form_data)

    response = client.post(reverse('password:share_password', kwargs={'slug': password.slug}), data=form_data)
    assert response.status_code == 200
    # Отладочное сообщение для проверки статуса ответа
    print("Response status code:", response.status_code)
    assert len(mail.outbox) == 1
    assert mail.outbox[0].subject == f"{form_data['name']} recommends you read {password.title}"
    assert f"Take password: {password.psw}" in mail.outbox[0].body
    assert form_data['comments'] in mail.outbox[0].body
