import os
import configparser

DEBUG = True
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

config = configparser.RawConfigParser()
config.read(os.path.join(BASE_DIR, 'config.ini'))

SECRET_KEY = config['GENERAL']['secret_key']

ALLOWED_HOSTS = ['localhost']

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Taipei'

USE_I18N = True

USE_L10N = True

USE_TZ = True

ROOT_URLCONF = 'web.urls'
STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# We do this so that django's collectstatic copies or our bundles to the STATIC_ROOT or syncs them to whatever storage we use.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# Application definition
#! order matters
INSTALLED_APPS = [
    # django app
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # third party app
    'security',
    'livereload',
    'webpack_loader',
    # custom app
    'example',
    ]

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'guardian.backends.ObjectPermissionBackend',
    )

MIDDLEWARE_CLASSES = [
     # django
    'django.middleware.security.SecurityMiddleware',
#   'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 3rd party
    'livereload.middleware.LiveReloadScript',
    'security.middleware.DoNotTrackMiddleware',
    'security.middleware.ContentNoSniff',
    'security.middleware.XssProtectMiddleware',
    'security.middleware.XFrameOptionsMiddleware',
    ]

# use jade as template engine
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'example/templates'),
            ],
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                ],
            'loaders': [
                ('pyjade.ext.django.Loader', (
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                    ))
                ],
            'builtins': ['pyjade.ext.django.templatetags'],
            },
    },
]

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql',
    #     'NAME': config['DATABASE']['name'],
    #     'USER': config['DATABASE']['username'],
    #     'PASSWORD': config['DATABASE']['password'],
    #     'HOST': config['DATABASE']['host'],
    #     'PORT': config['DATABASE']['port'],
    #     }
    # }
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

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

WEBPACK_LOADER = {
    'DEFAULT': {
        'CACHE': not DEBUG,
        'BUNDLE_DIR_NAME': 'bundles/',
        'STATS_FILE': os.path.join(BASE_DIR, 'webpack/webpack-stats.json'),
        'POLL_INTERVAL': 0.1,
        'IGNORE': ['.+\.hot-update.js', '.+\.map']
        }
    }
