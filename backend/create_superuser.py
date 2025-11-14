import os
from django.contrib.auth import get_user_model
from django.db import IntegrityError

User = get_user_model()

username = os.environ.get("DJANGO_SUPERUSER_USERNAME")
email = os.environ.get("DJANGO_SUPERUSER_EMAIL")
password = os.environ.get("DJANGO_SUPERUSER_PASSWORD")

if username and password:
    try:
        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(
                username=username,
                email=email,
                password=password
            )
            print("Superuser created successfully.")
        else:
            print("Superuser already exists.")
    except IntegrityError:
        print("Superuser already exists.")
else:
    print("Superuser environment variables missing.")
