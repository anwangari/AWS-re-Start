import boto3

def lambda_handler(event, context):
    # initialize s3 client
    s3 = boto3.client("s3")
    bucket_name = "bucket-wc"
    object_key = "KEY.txt" #event["Records"][0]["s3"]["object"]["key"]
    
    # get the file from the bucket
    file = s3.get_object(Bucket=bucket_name, Key=object_key)
    
    # read file contents into a variable
    file_content = file["Body"]
    
    # convert file_content to string
    text = ""
    for x in file_content:
        text = text + str(x)

    # count number of words in the file
    print(text)
    count = text.strip().count(" ") + 1
    
    message = f"The word count in the file {object_key} is {count}"
    
    # Initiate sns client
    sns = boto3.client("sns")
    
    # publish message to an sns topic
    sns.publish(TopicArn="arn:aws:sns:us-west-2:155594216162:topic-wordcount", Message=message)
    
    return message
