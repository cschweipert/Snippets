import boto3

# use Amazon S3
s3 = boto3.resource("s3")

# print bucket names
for bucket in s3.buckets.all():
    print(bucket.name)
    
# Create an S3 access object
s3 = boto3.client("s3")

# download script
s3.download_file(
    Bucket="cschweipert.watersheds", # The name of the bucket to download from
    Key="elevation.tiff", # The name of the key to download from (filename to download)
    Filename="download_from_s3/elevation.tiff" # The path to the file to download to
)

# upload script
s3.upload_file(
    Filename="download_from_s3/elevation2.tiff", # The path to the file to upload
    Bucket="cschweipert.watersheds", # The name of the bucket to upload to
    Key="elevation2.tiff", # The name of the key to upload to (filename to upload)
)