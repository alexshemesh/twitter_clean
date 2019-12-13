from pkg.twitter_client import create_bearer_token

def test_create_bearer_token():
    consumer_id = 'xvz1evFS4wEEPTGEFPHBog'
    consumer_secret = 'L8qq9PZyRg6ieKGEKhZolGC0vJWLw8iEJ88DRdyOg'
    result = create_bearer_token(consumer_id=consumer_id, consumer_secret=consumer_secret)
    assert result == b'eHZ6MWV2RlM0d0VFUFRHRUZQSEJvZzpMOHFxOVBaeVJnNmllS0dFS2hab2xHQzB2SldMdzhpRUo4OERSZHlPZw=='


def test_post_request():
    