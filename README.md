# Cloudwatch
  
Module to connect to AWS Cloudwatch  

*Read this in other languages: [English](README.md), [Português](README.pr.md), [Español](README.es.md)*

## How to install this module
  
To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.  


## Overview


1. Connect to AWS  
This command allows you to connect to your AWS account, for this you need your Access Key Id and your Secret Access Key, you can get this data in the AWS console, in the Security Credentials section.

2. Create Log Group  
This command allows you to create a log group in Cloudwatch. You must have the IAM permission: "logs: CreateLogGroup"

3. Delete Log Group  
This command allows you to delete a log group in Cloudwatch. You must have the IAM permission: "logs:DescribeLogGroups"

4. Create Log Stream  
This command allows you to create a log stream in Cloudwatch. You must have the IAM permission: "logs:CreateLogStream"

5. Delete Log Stream  
This command allows you to delete a log stream in Cloudwatch. You must have the IAM permission: "logs:DescribeLogStreams".

6. Put Log Events  
This command allows you to load log events into a log stream in Cloudwatch. You must have IAM permission: "logs:PutLogEvents".

7. Get Log Events  
This command allows you to get log events from a log stream in Cloudwatch. You must have IAM permission: "logs:GetLogEvents".  




----
### OS

- windows
- mac
- docker

### Dependencies
- [**boto3**](https://pypi.org/project/boto3/)
### License
  
![MIT](https://camo.githubusercontent.com/107590fac8cbd65071396bb4d04040f76cde5bde/687474703a2f2f696d672e736869656c64732e696f2f3a6c6963656e73652d6d69742d626c75652e7376673f7374796c653d666c61742d737175617265)  
[MIT](http://opensource.org/licenses/mit-license.ph)