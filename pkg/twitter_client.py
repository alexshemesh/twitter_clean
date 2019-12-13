import base64
import requests


class TwitterApi():
    def __init__(self, consumer_id: str, cosumer_secret: str):
        self.consumer_id = consumer_id
        self.cosumer_secret = cosumer_secret

    def percent_encoding(self, string):
        result = ''
        accepted = [c for c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-._~'.encode('utf-8')]
        for char in string.encode('utf-8'):
            result += chr(char) if char in accepted else '%{}'.format(hex(char)[2:]).upper()
        return result

    def create_bearer_token(self):
        consumer_id_RFC1738 = percent_encoding( self.consumer_id )
        consumer_secret_RFC1738 = percent_encoding( self.consumer_secret )
        brearer_token = '{}:{}'.format( consumer_id_RFC1738, consumer_secret_RFC1738 )
        base64_encoded = base64.b64encode( brearer_token.encode() )
        return base64_encoded

    def obtain_access_token(self, bearer_token :str):
        headers = {'ContTypeent-Type': 'application/x-www-form-urlencoded;charset=UTF-8', 
        'Accept-Encoding': 'gzip'}
        url = 'https://api.twitter.com/oauth2/token'
        try:
            r = requests.post(url, headers=headers)
        except Exception as e:
            print(e)
        return r['data']