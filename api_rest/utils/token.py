import jwt
from datetime import datetime, timedelta, timezone
from django.conf import settings

def generate_token(user_email):
    expiration = datetime.now(timezone.utc) + timedelta(minutes=180)
    payload = {
        'user_email': user_email,
        'exp': expiration,
        'iat': datetime.now(timezone.utc)
    }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
    return token