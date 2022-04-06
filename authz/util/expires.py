from authz.util import now
from authz.config import Config
from datetime import timedelta

def user_expires_at():
    return now() + timedelta(days = Config.USER_DEFAULT_EXPIRES_TIME)