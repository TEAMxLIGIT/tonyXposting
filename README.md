Certainly, here's an updated README.md file with your requested changes:

```markdown
# Tony - Auto Posting Userbot

![Tony Logo](https://te.legra.ph/file/89569cfe6abf0f52a5477.jpg)

Tony is an auto-posting userbot built with Pyrogram. It enables automated posting of messages to multiple groups and provides additional features.

## Features

- **Post Messages**: Schedule and post messages to various groups.
- **Broadcast Messages**: Broadcast messages or media to all connected groups.
- **Spam Limit Checker**: Check if the userbot is currently limited by using the `,"/limit` command.
- **Join/Leave Groups**: Join or leave groups using the `,"/join` and `,"/leave` commands.
- **Alive Status**: Get the current status of the userbot using the `,"/alive` command.
- **Message All Users**: Send a message to all recent users in the same group using the `,"/msgall` command.
- **Bot Commands**: Interact with the userbot using commands starting with `,"/"` or `,"."`.
- **Help Command**: Access one-line information about all the modules using the `,"/help` or `,"."help` command.

## Getting Started

### Prerequisites

- Python 3.6 or higher
- Install the required dependencies using `pip install -r requirements.txt`

### Configuration

1. Copy `config_sample.py` to `config.py` and update the required values.
2. Add your Pyrogram API ID, API Hash, Bot Token, and Owner ID in `config.py`.

### Running the Userbot

```bash
python -m Tony
```

### Deploying on Heroku

1. Create a new Heroku app.
2. Set the necessary environment variables (API_ID, API_HASH, BOT_TOKEN, OWNER_ID) in the Heroku app settings.
3. Deploy the app using the Heroku CLI or connect your GitHub repository to automatically deploy changes.

### Deploying on a VPS

1. Clone the repository to your VPS.
2. run this command python3 -m pip install --upgrade pip && pip3 install -r requirements.txt
2. Set the necessary environment variables (API_ID, API_HASH, BOT_TOKEN, OWNER_ID) in your VPS environment.
3. Run the userbot using `python3 -m Tony`.


## License

This project is licensed under the [MIT License](LICENSE).

[![License](https://www.gnu.org/graphics/gplv3-or-later.png)](LICENSE)   
SpamX is licensed under [GNU Affero General Public License](https://www.gnu.org/licenses/gplv3-or-later.pngl) v3 or later.


## Acknowledgments

- Thanks to the Pyrogram library developers for providing a powerful and easy-to-use Telegram API wrapper.
```

Feel free to modify it further to better suit your project's specific details and requirements.