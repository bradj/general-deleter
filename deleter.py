import requests
import sys
import time

payload = {'token': 'INSERT_YOUR_TOKEN_HERE'}

list_api = 'https://slack.com/api/channels.list'
history_api = 'https://slack.com/api/channels.history'
delete_message_api = 'https://slack.com/api/chat.delete'

def handle_error(error):
  if error == 'ratelimited':
    seconds = 10
    print('Waiting {} seconds and trying again'.format(seconds))
    time.sleep(seconds)

    return True

  return False


def post_request(url, data=None):
  r = requests.post(url, data=data)

  json_response = r.json()

  if json_response['ok'] is False:
    print(json_response)
    
    if handle_error(json_response['error']) is False:
      sys.exit(1)

  return json_response

def get_request(url, params=None):
  r = requests.get(url, params=params)

  json_response = r.json()

  if json_response['ok'] is False:
    print(r.json())
    sys.exit(1)

  return json_response

def get_channel_id(channel):
  r = get_request(list_api, payload)

  channels = r['channels']

  channel = [x for x in channels if x['name'] == channel][0]
  return channel['id']

def get_channel_messages(channel_id):
  params = payload

  params['channel'] = channel_id

  r = get_request(history_api, params)

  messages = r['messages']

  return messages

def delete_message(channel_id, ts):
  data = payload

  data['channel'] = channel_id
  data['ts'] = ts

  r = post_request(delete_message_api, data)

  print('Deleted {}'.format(ts))

general_id = get_channel_id('general')

messages = get_channel_messages(general_id)

for message in messages:
  delete_message(general_id, message['ts'])
