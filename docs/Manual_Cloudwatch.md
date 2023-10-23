# Cloudwatch
  
Module to connect to AWS Cloudwatch  

*Read this in other languages: [English](Manual_Cloudwatch.md), [Português](Manual_Cloudwatch.pr.md), [Español](Manual_Cloudwatch.es.md)*
  
![banner](imgs/Banner_Cloudwatch.png o jpg)
## How to install this module
  
To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.  


## Description of the commands

### Connect to AWS
  
This command allows you to connect to your AWS account, for this you need your Access Key Id and your Secret Access Key, you can get this data in the AWS console, in the Security Credentials section.
|Parameters|Description|example|
| --- | --- | --- |
|Access Key ID|AWS account identifier|IKAMLSURT6HYUHRY48EF|
|Secret Access Key|AWS account secret key|JYFifnrufd2pGHJ2illrZMVnhwxQnHSY5JK6JdhCtu|
|Region|AWS Region|us-east-1|
|Assign result to a Variable|Variable where the state of the connection will be stored, returns True if it is successful or False otherwise|Variable|

### Create Log Group
  
This command allows you to create a log group in Cloudwatch. You must have the IAM permission: "logs: CreateLogGroup"
|Parameters|Description|example|
| --- | --- | --- |
|Log group name|Name of the log group to create|new_log_group|
|Assign result to a Variable|Variable where the result will be stored, returns True if successful or False otherwise|Variable|

### Delete Log Group
  
This command allows you to delete a log group in Cloudwatch. You must have the IAM permission: "logs:DescribeLogGroups"
|Parameters|Description|example|
| --- | --- | --- |
|Log group name|Name of the log group to delete|log_group_name|
|Assign result to a Variable|Variable where the result will be stored, returns True if successful or False otherwise|Variable|

### Create Log Stream
  
This command allows you to create a log stream in Cloudwatch. You must have the IAM permission: "logs:CreateLogStream"
|Parameters|Description|example|
| --- | --- | --- |
|Log group name|Name of the log group where the stream will be created. Must exist previously.|log_group_name|
|Log stream name|Name of the log stream that will be created.|log_stream_name|
|Assign result to a Variable|Variable where the result will be stored, returns True if successful or False otherwise|Variable|

### Delete Log Stream
  
This command allows you to delete a log stream in Cloudwatch. You must have the IAM permission: "logs:DescribeLogStreams".
|Parameters|Description|example|
| --- | --- | --- |
|Log group name|Name of the log group where the stream to be deleted is located. It must exist previously.|log_group_name|
|Log stream name|Name of the log stream to be deleted.|log_stream_name|
|Assign result to a Variable|Variable where the result will be stored, returns True if successful or False otherwise|Variable|

### Put Log Events
  
This command allows you to load log events into a log stream in Cloudwatch. You must have IAM permission: "logs:PutLogEvents".
|Parameters|Description|example|
| --- | --- | --- |
|Log group name|Name of the log group where the stream is located.|log_group_name|
|Log stream name|Name of the log stream where you want to put the events.|log_stream_name|
|Log events|Log events that you want to put in the stream.|[{
  "timestamp": 123456789,
  "message": "This is a test message"
}, {
  "timestamp": 123456789,
  "message": "This is another test message"
}]|
|Rocketbot log file|Name of the log stream that you want to get the token.|C:/Rocketbot/logs/log.txt|
|Assign result to a Variable|Variable where the result will be stored, returns the token of the log stream if executed correctly or False otherwise.|Variable|

### Get Log Events
  
This command allows you to get log events from a log stream in Cloudwatch. You must have IAM permission: "logs:GetLogEvents".
|Parameters|Description|example|
| --- | --- | --- |
|Log group name|Name of the log group where the stream is located.|log_group_name|
|Log stream name|Name of the log stream that you want to get the events.|log_stream_name|
|Assign result to a Variable|Variable where the result will be stored, returns a dictionary with the events of the log stream if executed correctly or False otherwise.|Variable|
