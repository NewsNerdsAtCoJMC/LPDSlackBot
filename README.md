# LPDSlackBot
A Slack Bot that will respond with crime statistics from the Lincoln, Neb. Police Department.

## Slack Bot Guide
This requires both [slackbotguide.py](slackbotguide.py) and [LPDdispatch.sqlite](LPDdispatch.sqlite) to be downloaded to the same directory.

You will need to edit the python file to include your bot's ID and your API key. If you want to use the `weather` function, you will also need a [Dark Sky API key](https://darksky.net/dev/). If you don't plan to use the `weather` function, delete the `WEATHER_KEY = os.environ.get("WEATHER_TOKEN")` line.

### Slack Bot ID and API Key
You will first need to create a bot. Go [here](https://newsnerdscojmc.slack.com/apps/new/A0F7YS25R-bots) and fill out the information. It will then give you your API token. Copy that and paste it at the top of the script, replacing `os.environ.get("SLACK_BOT_TOKEN")`.

To get the Bot ID, you'll need to query the API. 

* Make sure you have slackclient installed. Run `sudo pip install slackclient` in your terminal.
* Create a new file named `print_bot_id.py` and fill it with the following code.

```
from slackclient import SlackClient


BOT_NAME = 'starterbot'

slack_client = SlackClient('SLACK_BOT_TOKEN')


if __name__ == "__main__":
    api_call = slack_client.api_call("users.list")
    if api_call.get('ok'):
        # retrieve all users so we can find our bot
        users = api_call.get('members')
        for user in users:
            if 'name' in user and user.get('name') == BOT_NAME:
                print("Bot ID for '" + user['name'] + "' is " + user.get('id'))
    else:
        print("could not find bot user with the name " + BOT_NAME)
```

* Replace `'starterbot'` with the name of your bot
* Replace `'SLACK_BOT_TOKEN'` with your API key

This script will get a list of users from Slack and return the ID associated with your bot. Just run `python print_bot_id.py` in your terminal. The printed response is your Bot ID.

You can now replace `os.environ.get("BOT_ID")` with your Bot ID and `os.environ.get("SLACK_BOT_TOKEN")` with your API key.

### Running the bot
CD into the directory with [slackbotguide.py](slackbotguide.py) and [LPDdispatch.sqlite](LPDdispatch.sqlite) in your terminal. Then, run `python slackbotguide.py`.

You should see `Bot connected and running!`. This means your bot is now listening for any mentions of its name. Invite your bot to a Slack channel and send it a command.

When you are done running your bot, switch back to your terminal and press `Ctrl+C`. This will shut down the process.
