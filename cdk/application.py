from aws_cdk import (
    Stack,
    CfnParameter
)
import aws_cdk.aws_apprunner_alpha as apprunner

from constructs import Construct


class InfrastructureStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        apprunner_source_connection_arn_parameter = CfnParameter(
            self,
            "SourceConnectionArn"
        )
        service = apprunner.Service(self, "whats_my_weather",
                                    source=apprunner.Source.from_git_hub(
                                        repository_url="https://github.com/s0enke/aws-serverless-apprunner-django-sample",
                                        branch="main",
                                        configuration_source=apprunner.ConfigurationSourceType.REPOSITORY,
                                        connection=apprunner.GitHubConnection.from_connection_arn(
                                            apprunner_source_connection_arn_parameter.value_as_string
                                        )
                                    )
                                    )
        cfn_service = service.node.default_child
        cfn_service.add_property_override('SourceConfiguration.AutoDeploymentsEnabled', True)
