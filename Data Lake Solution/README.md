# Data Lake Setup with Amazon S3, Lake Formation, and Glue
This repository contains the data and instructions for setting up a data lake using Amazon S3, AWS Lake Formation, and AWS Glue. The data lake infrastructure allows organizations to store, manage, and analyze large volumes of structured and unstructured data.

## Overview
In today's data-driven world, businesses deal with massive amounts of data from various sources. A data lake provides a centralized repository for storing and processing this data, enabling organizations to derive valuable insights and drive data-driven initiatives.

This repository provides step-by-step instructions on how to create a data lake using the following AWS services:

- Amazon S3: Scalable and durable storage for data.
- AWS Lake Formation: Simplifies setup, management, and data governance of the data lake.
- AWS Glue: Provides data cataloging, data ingestion, and transformation capabilities.

## Usage
To use the data and follow along with the setup process, please follow these steps:
### 1. Set up an Amazon S3 bucket:
  - Log in to the AWS Management Console.
  - Navigate to the S3 service.
  - Create a new bucket with a unique name, e.g., **my-datalake10**.
  - Within the bucket, create the following folders: **data** and **script**.

### 2. Upload data to the S3 bucket:
  - Within the **data** folder, create two subfolders: **customers** and **sales**.
  - Upload the respective CSV files, "customers.csv" and "sales(1).csv", into their corresponding subfolders.

### 3. Set up IAM users and roles:
  - Create two IAM users, 'customer_user_Karanja' and 'sales_user_Maina', with the necessary permissions. Refer to the article for detailed instructions.

### 4. Configure AWS Lake Formation:
  - Set up a Data Lake Administrator.
  - Register the S3 storage location.
  - Create the database.
  - Define data lake permissions.

### 5. Perform data cataloging with AWS Glue:
  - Create an AWS Glue Crawler to analyze the data in the S3 bucket and create metadata tables.
  - Explore the created tables in the AWS Glue Data Catalog.

### 6. Query data with Amazon Athena:
  - Configure the "Query result location" in the Athena console.
  - Use the provided queries to analyze the data in the data lake.

## Account Clean-up
To avoid additional charges, it is recommended to clean up the resources created during the setup process. Follow these steps:
 - Delete the '**dojocrawler**' crawler in the AWS Glue Console.
 - Delete the '**dojodb**' database in the AWS Lake Formation Console.
 - Delete the **s3://my_datalake10/data** location configured as the Data lake location in the AWS Lake Formation Console.
 - Delete the **s3://my_datalake10/data** bucket in the S3 Management Console.
 - Delete the IAM Role - **dojocrawlerrole**.
 - Delete the IAM Users - **sales_user_Maina** and **customers_user_Karanja**.

Please note that deleting these resources is irreversible, so make sure to back up any important data before proceeding with the clean-up.

For a detailed walkthrough and more information, refer to the [original article](https://medium.com/@anwangari/simplified-infrastructure-provisioning-with-aws-cloudformation-vpc-and-ec2-instance-bd47195f3320) on creating a data lake with Amazon S3, Lake Formation, and Glue.

