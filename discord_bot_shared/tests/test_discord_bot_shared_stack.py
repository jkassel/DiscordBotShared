import os
import sys
import pytest
from aws_cdk import App
from aws_cdk.assertions import Template

# Add the `src/cdk` directory to sys.path so imports work
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src/cdk")))
from discord_bot_shared_stack import DiscordBotSharedStack  # noqa: E402


@pytest.fixture
def cdk_template():
    """Synthesizes the CDK stack and returns its CloudFormation template."""
    app = App()

    # Set environment variables (simulating `.env` usage)
    os.environ["AWS_ACCOUNT"] = "123456789012"
    os.environ["AWS_REGION"] = "us-east-1"
    os.environ["APP_NAME"] = "TestDiscordBotApp"

    # Create the stack
    stack = DiscordBotSharedStack(
        app,
        f"{os.getenv('APP_NAME')}DiscordBotSharedStack",
        app_name=os.getenv("APP_NAME"),
    )

    # Generate the CloudFormation template
    template = Template.from_stack(stack)
    return template


def test_api_gateway_created(cdk_template):
    """Test if the API Gateway is created."""
    cdk_template.resource_count_is("AWS::ApiGatewayV2::Api", 1)


def test_api_gateway_outputs(cdk_template):
    """Test if the API Gateway ID and Endpoint are exported."""
    cdk_template.has_output("ApiGatewayIdOutput", {})
    cdk_template.has_output("ApiGatewayEndpointOutput", {})
