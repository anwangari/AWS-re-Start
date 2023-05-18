# CloudFormation Template: TrialVPC with EC2 Instance
This CloudFormation template allows you to quickly provision a TrialVPC with an EC2 instance named TrialServer. The template creates a VPC, an Internet Gateway, a public subnet, a route table, a subnet association, a security group, and an EC2 instance running an Apache web server.

## Prerequisites
Before using this template, ensure that you have the following:

 - An AWS account with sufficient permissions to create resources.
 - Basic familiarity with AWS

## Usage
To deploy the TrialVPC and EC2 instance, follow these steps:

1. Open the AWS Management Console and navigate to the CloudFormation service.
2. Click on "Create Stack" and choose "With new resources (standard)".
3. Select "Upload a template file" and upload the **"trial-vpc-ec2-template.yaml"** file.
4. Provide a unique stack name and fill in any required parameters or leave them with their default values.
5. Review the configuration and click "Create stack" to initiate the deployment.
6. Wait for the CloudFormation stack to be created. This process may take a few minutes.
7. Once the stack creation is complete, you can access the EC2 instance using its public IP address or DNS name.

## Stack Outputs
The CloudFormation stack provides the following outputs:
- **EC2InstancePublicIP**: The public IP address of the EC2 instance.

## Customizing the Template
If you need to customize the template, you can modify the parameters or resources defined in the CloudFormation template file (**trial-vpc-ec2-template.yaml**). You can adjust the VPC CIDR block, subnet CIDR block, security group rules, EC2 instance type, and other properties to suit your requirements.

## Cleaning Up
To delete the resources created by this CloudFormation template, follow these steps:

1. Open the AWS Management Console and navigate to the CloudFormation service.
2. Select the stack created from this template.
3. Click on "Actions" and choose "Delete stack".
4. Confirm the deletion when prompted.
5. Wait for the stack deletion process to complete. This may take a few minutes.

Please note that deleting the stack will remove all the resources provisioned by the template, including the VPC, Internet Gateway, subnet, security group, and EC2 instance.

## Conclusion
This template serves as a starting point for building more complex infrastructure configurations using AWS CloudFormation.

## Contact

For any questions or suggestions, please contact:

- [Anthony Njuguna](mailto:antonnm7@gmail.com)

