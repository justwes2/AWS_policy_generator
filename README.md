# AWS Application Team Policy Generator

The purpose of this tool is to rapidly generate identical policies for application teams working in AWS. Using managed policies, a user can create a role or group for each team, and by attaching policies with conditions, prevent users from affecting instances that are not tagged for their application.

Future improvements include:
- incorporate boto3 to automatically push policies to AWS
- automate version control each time the tool runs so that previous versions of policies can be reviewed
- using boto3, policies should automatically be added to roles/groups based on app name. 
