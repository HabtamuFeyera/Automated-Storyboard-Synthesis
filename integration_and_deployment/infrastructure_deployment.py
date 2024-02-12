import boto3

# Create an Elastic Beanstalk application
eb = boto3.client('elasticbeanstalk')
response = eb.create_application(ApplicationName='StoryboardApp')

# Create an environment for the application
response = eb.create_environment(
    ApplicationName='StoryboardApp',
    EnvironmentName='StoryboardEnv',
    SolutionStackName='64bit Amazon Linux 2 v5.4.0 running Python 3.8',
    OptionSettings=[
        {
            'Namespace': 'aws:autoscaling:launchconfiguration',
            'OptionName': 'InstanceType',
            'Value': 't2.micro'
        }
    ]
)
