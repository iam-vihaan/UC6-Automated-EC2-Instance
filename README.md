# UC6-Automated-EC2-Instance

Use case 6: Serverless EC2 Instance Scheduler for Company Working Hours

Title: Automated EC2 Instance Management

Objective:

To optimize the operational costs and efficiency of EC2 instances by automating their start and stop processes based on company working hours using AWS Lambda and CloudWatch Events.

In some companies, there is no need to run their EC2 instances 24/7; they require instances to operate during specific time periods, such as company working hours, from 8:00 AM in the morning to 5:00 PM in the evening. To address this scenario, I will implement two Lambda functions responsible for starting and stopping instances. These Lambda functions will be triggered by two CloudWatch Events in the morning and evening. This solution is fully serverless.


Output:

1. Target architecture

2. Target Technology Stack

3. Implementation (AWS UI/ Terraform Script)

4. Create an understanding document based on implementation

Part II

Create GitHub Action Workflow file that triggers on push to the main branch.

The workflow should:

· Set up Terraform

· Initialize Terraform

· Generate Terraform Plan

· Include all Best practices(Terraform test, split state file, policy as code etc) Ref link: mathesh-me/serverless-ec2-scheduler: Creating a automation solution for EC2 instance scheduling
