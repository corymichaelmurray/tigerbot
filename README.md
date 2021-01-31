# tigerbot
a bot for the hahnville gaming server

## development
to contribute, get yourself a discord token and set it as an environment variable. 
if you're using VSCode, you can set up the environment variable in the `.vscode/launch.json` file and use the built in debugger after opening the directory in the IDE.

to get started, install Python 3 and use `virtualenv` to set up your environment.
```
virtualenv tigerbot
```
then, enter your environment and install the project with:
```
source tigerbot/bin/activate
pip3 install -r requirements.txt
```

to keep this project easy to maintain, follow the Cogs convention found in the [discord api docs](https://discordpy.readthedocs.io/en/latest/ext/commands/cogs.html) and add any functionality in its own directory. for example, if you are adding a poll functionality, making a `utilities` folder with a `poll.py` file with a `Poll(commands.Cog)` class inside the file would be a great start.

### notes
- set ToS message from Discord as admin
- create poll functionality
- mod tools
