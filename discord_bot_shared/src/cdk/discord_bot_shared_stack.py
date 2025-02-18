from aws_cdk import Stack, CfnOutput, aws_apigatewayv2 as apigw, Duration
from constructs import Construct


class DiscordBotSharedStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, app_name: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        http_api = apigw.HttpApi(
            self,
            f"{app_name}DiscordBotHttpApi",
            cors_preflight=apigw.CorsPreflightOptions(
                allow_methods=[apigw.CorsHttpMethod.POST],
                allow_origins=["*"],
                allow_headers=[
                    "content-type",
                    "x-signature-ed25519",
                    "x-signature-timestamp",
                ],
                max_age=Duration.days(10),
            ),
        )

        CfnOutput(
            self,
            "ApiGatewayIdOutput",
            value=http_api.http_api_id,  # or http_api.http_api_id for HTTP API
            export_name="ApiGatewayId",
        )

        CfnOutput(
            self,
            "ApiGatewayEndpointOutput",
            value=http_api.api_endpoint,  # or http_api.http_api_id for HTTP API
            export_name="ApiGatewayEndpoint",
        )
