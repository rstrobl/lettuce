DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'jilo-db.sqlite3',
    }
}

SECRET_KEY = 'vkdp##3sxiy0m7pzenbucgrqq#3v7d(mg6jtwkhi#uw5p0er4s'

ROOT_URLCONF = 'jilo.urls'

INSTALLED_APPS = (
    'lettuce.django',
    'fruits',
)
