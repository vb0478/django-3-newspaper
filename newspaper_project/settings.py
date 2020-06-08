"""
Django settings for newspaper_project project.

Generated by 'django-admin startproject' using Django 3.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'y=sh7e8^s_6_s=9410be@js$a9+3#sq(0pkey5zyx-$(vsmm+8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # locals
    'users.apps.UsersConfig',
    'pages.apps.PagesConfig',
    'articles.apps.ArticlesConfig'
    # 3rd party
    'crispy_forms',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'newspaper_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')], # new dir
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'newspaper_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

# use the AUTH_USER_MODEL config to tell Django to use our new custom user model
# in place of the built-in User model:
AUTH_USER_MODEL = 'users.CustomUser' # new

# newspaper_project/settings.py
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

# Working with forms is a challenge and django-crispy-forms makes it easier to write DRY code.
# pipenv install django-crispy-forms==..
# Since we’re using Bootstrap4 we should also add that config to our settings.py file.
CRISPY_TEMPLATE_PACK = 'bootstrap4'
# Now in our signup.html template we can quickly use crispy forms.

# In production we’ll use the email service SendGrid to actually send the emails
# but for testing purposes we can rely on Django’s console backend setting
# which outputs the email text to our command line console instead.
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# after regisgration on SendGrid or MailGun:
# Web API or SMTP Relay.
# We’ll use SMTP since it is the simplest and works well for our basic needs here.
# In a large-scale website you likely would want to use the Web API instead
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' # new
#EMAIL_HOST = 'smtp.sendgrid.net'
#EMAIL_HOST_USER = 'apikey'
#EMAIL_HOST_PASSWORD = 'sendgrid_password'
#EMAIL_PORT = 587
#EMAIL_USE_TLS = True

# custom email:
# In this case, I knew what text Django was using by default
# but it wasn’t clear where in the Django source code it was written.
# all of Django’s source code is available on Github
# Use the Github search bar and enter a few words from the email text.
# The first result is the one we want. It shows the code is located at
# django/contrib/\ admin/templates/registration/password_reset_email.html
# Let’s change it.
# $ touch templates/registration/password_reset_email.html
