ALLOWED_HOSTS = ["*"]

# Modules in use, commented modules that you won't use
MODULES = [
    'authentication',
    'base',
    'booth',
    'census',
    'mixnet',
    'postproc',
    'store',
    'visualizer',
    'voting',
]

APIS = {
    'authentication': 'BASEURL',
    'base': 'BASEURL',
    'booth': 'BASEURL',
    'census': 'BASEURL',
    'mixnet': 'BASEURL',
    'postproc': 'BASEURL',
    'store': 'BASEURL',
    'visualizer': 'BASEURL',
    'voting': 'BASEURL',
}

BASEURL = 'http://localhost:8000'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'decidedb',
        'USER': 'decide',
	'PASSWORD': 'complexpassword'
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# number of bits for the key, all auths should use the same number of bits
KEYBITS = 256
