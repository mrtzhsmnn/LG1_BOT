# LG1_BOT
Discord bot for the famous LG1 server.

Following the official documentation closely:
https://discordpy.readthedocs.io/

Also following the commit guidelines:
https://www.conventionalcommits.org/en/v1.0.0/

## bot.py file
Main bot file, this contains the brains of the bot.

## envkeys.py file 
Questionable implementation to avoid using enviromental variables.
To use the bot you need a similiarly build .py file that you import.
```python
def TOKEN():
    return '[YOUR_TOKEN]'
```
