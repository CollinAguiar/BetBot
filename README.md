# BetBot
## Setup

1. **Add your bot token**  
   Open bot_config.py and replace:
   TOKEN = ""
2. **Scopes, Permissions, and Intents**
   When adding the bot to your server, make sure it has these scopes:
   - bot
   - applications.commands
   And these permissions:
   - Send messages
   - Embed links
   - Read Message History
   And these intents:
   - Server Members Intent --> On
   - Message Content Intent --> On
3. **Run the bot with python3 main.py**
