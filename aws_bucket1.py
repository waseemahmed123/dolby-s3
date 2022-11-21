import boto3
import botocore.exceptions
import logging
import os

access_key="AKIAYQLEORWSKGEXTDAB"
secret_access_key="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"
client=boto3.client("s3",
aws_access_key_id=access_key,
aws_secret_access_key=secret_access_key)


def upload_to_s3(file_path,bucket_name):
    try:
        file_name=os.path.basename(file_path)
        logging.logger("INFO, Name of file:".format(file_name))
        logging.logger("INFO", "File path :".format(file_path))
        logging.logger("INFO", "Bucket_Name:" .format(bucket_name))
     
        with open("file_path","rb") as file:
            client.upload_fileobj(file,bucket_name,file_name)
    except botocore.exceptions.ClientError as error:
        logging.logger("ERROR,error")


    

def create_s3_bucket():
    try:
        response=client.create_bucket(Bucket='ez-media-enhance-dev')

        if response["ResponseMetadata"]["HTTPStatusCode"]==200:
            logging.logger("INFO","Bucket Created Successfully")
        else:
            logging.logger("DEBUG","Bucket Not Created!!")
    except botocore.exceptions.ClientError as error:
        logging.logger("ERROR",error)

def logger(log_level,msg):
    logging.basicConfig(filename="logs/s3_app.log",encoding="utf-8",level=logging.DEBUG,
    format="%(asctime)s: %(levelname)s:%(message)s", datefmt="%m/%d/%Y %T:%M:%S")
    if log_level=="ERROR":
        logging.error(msg)
    elif log_level=="DEBUG":
        logging.debug(msg)
    elif log_level=="INFO":
        logging.info(msg)
    elif log_level=="WARNING":
        logging.warning(msg)

path=""
upload_to_s3(path, "bucket created successfully")
