DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'espinafre-db.sqlite3',
    }
}

SECRET_KEY = 'vkdp##3sxiy0m7pzenbi1ucgrqq#3v7!dx(mg6jtwkhi#uw5p0'

ROOT_URLCONF = 'espinafre.urls'

INSTALLED_APPS = (
    'lettuce.django',
    'south',
    'leaves',
)
