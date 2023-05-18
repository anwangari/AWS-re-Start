# Word Count Lambda Function
This Lambda function calculates the word count of a file stored in an Amazon S3 bucket and publishes the result to an Amazon SNS topic.

## Functionality
1. The Lambda function is triggered by an S3 event when a file is uploaded to the specified bucket.
2. It retrieves the file from the bucket and reads its contents.
3. The file contents are converted to a string and the word count is calculated.
4. The word count result is formatted into a message.
5. The message is published to an SNS topic.
6. The function returns the message.

## Prerequisites
- An AWS account with appropriate permissions to create and configure Lambda functions, S3 buckets, and SNS topics.
- Python and the 'boto3' library installed locally.

## Configuration
1. Create an S3 bucket to store the files.
2. Create an SNS topic to publish the word count results.
3. Configure the Lambda function with the appropriate IAM role, triggering it upon S3 events.
4. Update the **bucket_name** variable in the Lambda function code to match your S3 bucket's name.
5. Update the **TopicArn** parameter in the sns.publish method with your SNS topic's **ARN**.

## Deployment
1. Package and deploy the Lambda function to your AWS account.
2. Ensure the Lambda function is properly configured with the necessary permissions and triggers.
3. Upload files to the specified S3 bucket to trigger the Lambda function.
4. Check the SNS topic for the word count results.
5. Feel free to modify and customize the Lambda function code to fit your specific requirements.

## Contact

For any questions or further assistance, please contact:

- Name: [Anthony Njuguna](mailto:antonnm7@gmail.com)
