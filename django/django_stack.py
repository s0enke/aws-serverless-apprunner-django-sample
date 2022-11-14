from aws_cdk import (
    Stack,
    App
)
from constructs import Construct

class DjangoStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

