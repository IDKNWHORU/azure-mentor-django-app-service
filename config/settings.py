import os
from dotenv import load_dotenv
from pathlib import Path
from datetime import timedelta

load_dotenv()

AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_VERSION = os.getenv("AZURE_OPENAI_VERSION")
AZURE_OPENAI_DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT")

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-0fn7+z2s#7$jf9#r#0tgq^f^&3_c_e^+emgv@a#j@+=(reo8k4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]

# Application definition
INSTALLED_APPS = [
    'accounts',
    'chat',
    'common',
    'game',
    'image_gen',
    'llm',
    'storymode',
    'channels',
    'corsheaders',

    # djangorestframework-simplejwt
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_simplejwt.token_blacklist',

    # django-allauth
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.kakao',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.microsoft',

    # dj-rest-auth
    'dj_rest_auth',
    'dj_rest_auth.registration',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware', 
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    "allauth.account.middleware.AccountMiddleware",
]

# CORS
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_ORIGINS = [
    'http://127.0.0.1:8000/',
    'http://127.0.0.1:8081/'
]

# USER 모델
AUTH_USER_MODEL = 'accounts.User'

ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'

# auth
SITE_ID = 1

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

SOCIAL_AUTH_GOOGLE_CLIENT_ID = os.environ.get('SOCIAL_AUTH_GOOGLE_CLIENT_ID')
SOCIAL_AUTH_GOOGLE_CLIENT_SECRET = os.environ.get('SOCIAL_AUTH_GOOGLE_CLIENT_SECRET')
SOCIAL_AUTH_KAKAO_REST_API_KEY = os.environ.get('SOCIAL_AUTH_KAKAO_REST_API_KEY')
SOCIAL_AUTH_MICROSOFT_TENANT_ID = os.getenv('SOCIAL_AUTH_MICROSOFT_TENANT_ID')
SOCIAL_AUTH_MICROSOFT_CLIENT_ID = os.getenv('SOCIAL_AUTH_MICROSOFT_CLIENT_ID')
SOCIAL_AUTH_MICROSOFT_CLIENT_SECRET = os.getenv('SOCIAL_AUTH_MICROSOFT_CLIENT_SECRET')

SOCIALACCOUNT_PROVIDERS = {
    'google' : {
        'APP' : {
            'client_id' : SOCIAL_AUTH_GOOGLE_CLIENT_ID,
            'secret' : SOCIAL_AUTH_GOOGLE_CLIENT_SECRET,
            'key' : ''
        },
        'SCOPE' : ['profile', 'email'],
        'AUTH_PARAMS' : {
            'access_type' : 'online',
        }
    },
    'kakao' : {
        'APP' : {
            'client_id' : SOCIAL_AUTH_KAKAO_REST_API_KEY
        }
    },
    'microsoft': {
        'APPS': [
            {
                'client_id': SOCIAL_AUTH_MICROSOFT_CLIENT_ID,
                'client_secret': SOCIAL_AUTH_MICROSOFT_CLIENT_SECRET,
                'settings': {
                    'tenant': SOCIAL_AUTH_MICROSOFT_TENANT_ID,
                    'login_url': 'https://login.microsoftonline.com',
                    'graph_url': 'https://graph.microsoft.com',
                }
            }
        ]
    }
}

# JWT
REST_USE_JWT = True
SIMPLE_JWT = {
    # access 토큰 유효시간
    'ACCESS_TOKEN_LIFETIME' : timedelta(hours=1),
    # refresh 토큰 유효시간 timedelta
    'REFRESH_TOKEN_LIFETIME' : timedelta(hours=24),    
    # refresh 토큰 갱신 시, 새 토큰 생성
    'ROTATE_REFRESH_TOKENS' : False,
    # 토큰 생성 후, 이전 토큰 블랙리스트에 추가
    'BLACKLIST_AFTER_ROTATION' : True
}

# RestFramework
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_AUTHENTICATION_CLASSES' : (
        # 'rest_framework_simplejwt.authentication.JWTAuthentication',
        # 'path.to.authentication.CookieJWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
    )
}

# Channels (ASGI)
ASGI_APPLICATION = "config.asgi.application"

# Channels에서 WebSocket 지원을 위한 기본 채널 레이어 (추후 Redis 연결 예정)
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer"
    }
}

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "unique-snowflake",
    }
}

# AZURE_REDIS_CONNECTIONSTRING 환경 변수가 설정된 경우에만 Redis 캐시를 사용
AZURE_REDIS_CONNECTIONSTRING = os.environ.get('AZURE_REDIS_CONNECTIONSTRING')
if AZURE_REDIS_CONNECTIONSTRING:
    CACHES["default"] = {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": AZURE_REDIS_CONNECTIONSTRING,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }

# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases
DATABASE_USER = os.environ.get('DATABASE_USER')
DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD')
DATABASE_HOST = os.environ.get('DATABASE_HOST')
DATABASE_PORT = os.environ.get('DATABASE_PORT')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME' : 'project_test',
        'USER' : DATABASE_USER,
        'PASSWORD' : DATABASE_PASSWORD,
        'HOST' : DATABASE_HOST,
        'PORT' : DATABASE_PORT,
    },
    'prod': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME' : 'project',
        'USER' : DATABASE_USER,
        'PASSWORD' : DATABASE_PASSWORD,
        'HOST' : DATABASE_HOST,
        'PORT' : DATABASE_PORT,
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'ko-KR'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'