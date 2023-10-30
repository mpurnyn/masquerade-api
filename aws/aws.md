# AWS

Steps taken in setting up AWS components.

## IAM Identity Center
Setting up IAM seems to indicate that IAM Identity Center is the prefered method.
1. create a custom name https://facemasq.awsapps.com/start 
2. edit settings to require MFA and send a OTP
3. create a permission set with admin privilages
4. create a user and give them the admin permission set
5. test logging in

notes:
- still need to delve into the differences of IAM and IAM Identity center
- need to limit accounts to just specific resources
- need to limit budget

## S3
1. Set up a bucket for facemasqs
2. Uploaded some files
3. Tested accessing the files.

notes: 
- files only have a name and url, they are restricted by aws user credentials.
- files are easy to see for an administrator, maybe it would be better to find a solution that allows users to upload anonymously
- files access for the server will be for all files, but will need to be restricted by session with individual users in the app
- need to write code for CRUD operations for facemasq files on the s3 bucket
- need to write code for CRUD operations for videomasq files on the s3 bucket (may need strong security)

## AWS CLI
AWS can be access by local CLI by providing the right credentials
- some addons for vs code exist, will need to figure out which ones are useful
