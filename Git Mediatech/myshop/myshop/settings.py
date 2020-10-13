import os

#Chemin de base de mon Path 
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#Ma clé de securité pour ma future passerelle de paiement Stripe TODO
SECRET_KEY = 'ze6=6bnyczhxb2m)$elj#o(e6m85j%amr+aj6o3am*6j*aw2!t'

#Activation de mon mode debug 
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
    'shop.apps.ShopConfig',
    'cart.apps.CartConfig',
    'orders.apps.OrdersConfig',
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

ROOT_URLCONF = 'myshop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.context_processors.cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'myshop.wsgi.application'

#Donne l'id de mon pannier 
CART_SESSION_ID = 'cart'

#Id de connexion de base à ma base sqlite avec MangoDb
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

MEDIA_URL  = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

STATIC_URL = '/static/'

#A voir s'il ne serra pas judicieux de le passer en Fr
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ   = True

STATIC_URL = '/static/'
