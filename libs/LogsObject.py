import boto3
import os

class LogsObject:
    def __init__(self, awsAccessKeyId, awsSecretAccessKey, region):
        self.client = boto3.client(
            'logs',
            region_name=region,
            aws_access_key_id=awsAccessKeyId, 
            aws_secret_access_key=awsSecretAccessKey
        )

    # Function to know if the connection is established or not
    def getAccountPolicies(self):
        response = self.client.describe_account_policies(
            policyType='DATA_PROTECTION_POLICY'
        )
    
        return response

    def createLogGroup(self, name):
        response = self.client.create_log_group(
            logGroupName=name
        )

        return response

    def deleteLogGroup(self, name):
        response = self.client.delete_log_group(
            logGroupName=name
        )

        return response

    def createLogStream(self, logGroupName, logStreamName):
        response = self.client.create_log_stream(
            logGroupName=logGroupName,
            logStreamName=logStreamName
        )

        return response

    def deleteLogStream(self, logGroupName, logStreamName):
        response = self.client.delete_log_stream(
            logGroupName=logGroupName,
            logStreamName=logStreamName
        )

        return response

    def putLogEvents(self, logGroupName, logStreamName, logEvents):
        response = self.client.put_log_events(
            logGroupName=logGroupName,
            logStreamName=logStreamName,
            logEvents=logEvents
        )

        return response

    def getLogEvents(self, logGroupName, logStreamName):
        response = self.client.get_log_events(
            logGroupName=logGroupName,
            logStreamName=logStreamName
        )

        return response