from aws_cdk import (
    Stack,
)
import aws_cdk.aws_apprunner_alpha as apprunner

from constructs import Construct


class InfrastructureStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        service = apprunner.Service(self, "whats_my_weather",
                                    source=apprunner.Source.from_git_hub(
                                        repository_url="https://github.com/s0enke/aws-serverless-apprunner-django-sample",
                                        branch="master",
                                        configuration_source=apprunner.ConfigurationSourceType.REPOSITORY,
                                        connection=apprunner.GitHubConnection.from_connection_arn(
                                            "arn:aws:apprunner:eu-west-1:255296336815:connection/apprunner/59f079c743b94d5c98f5a619052d4ffb")
                                    )
                                    )
        cfn_service = service.node.default_child
        cfn_service.add_property_override('SourceConfiguration.AutoDeploymentsEnabled', True)
