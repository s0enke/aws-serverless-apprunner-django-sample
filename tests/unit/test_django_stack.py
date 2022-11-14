import aws_cdk as core
import aws_cdk.assertions as assertions

from django.django_stack import DjangoStack

# example tests. To run these tests, uncomment this file along with the example
# resource in django/django_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = DjangoStack(app, "django")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
