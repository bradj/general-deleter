# general-deleter

Deletes all messages in the provided slack channel

**Warning: I wrote this very quickly. Run at your own risk.**

## Requirements

1. [pipenv](https://pipenv.readthedocs.io/en/latest/)
1. Python 3.7

## Instructions

1. Clone repo
1. Replace `INSERT_YOUR_TOKEN_HERE` with your Slack Auth Token in `deleter.py`
1. Set `remove_messages_from` to channel you want to delete from
1. `pipenv install`
1. `pipenv run delete` - This will start deleting all messages in `general`

## Slack Endpoints

* https://slack.com/api/channels.list
* https://slack.com/api/channels.history
* https://api.slack.com/methods/chat.delete