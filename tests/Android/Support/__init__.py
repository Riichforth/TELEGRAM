import json

try:
    path = '{}/config.json'.format('/'.join(__file__.replace('\\', '/').split('/')[:-4]))
    CONFIG = json.load(open(path))
    APP_ID = CONFIG['capabilities'].get('appPackage')
except:
    CONFIG = None
    APP_ID = 'org.telegram.messenger'
