import os
from dotenv import load_dotenv
from aws_cdk import App, Environment
from discord_bot_shared_stack import DiscordBotSharedStack

# Load environment variables from .env file
load_dotenv()

app = App()

env = Environment(
    account=os.getenv("AWS_ACCOUNT"),
    region=os.getenv("AWS_REGION"),
)

app_name = os.getenv("APP_NAME")

DiscordBotSharedStack(
    app, f"{app_name}DiscordBotSharedStack", env=env, app_name=app_name
)

app.synth()
