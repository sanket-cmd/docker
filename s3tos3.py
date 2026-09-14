import boto3

client = boto3.client(
    's3',
    aws_access_key_id='xyz',
    aws_secret_access_key='abc',
    region_name='ap-south-1'
)
bucketname = 'my-demo-22-08-2026'
destinationBucket = 'destination-22-08-2026'


def copy_to_destination(fname):
    response = client.copy_object(Bucket='{}'.format(destinationBucket), CopySource='{}/{}'.format(bucketname, fname),
                                  Key='{}'.format(fname))


def delete_from_Source(fname):
    response = client.delete_object(Bucket='{}'.format(bucketname), Key='{}'.format(fname))


def main():
    response = client.list_objects(Bucket='{}'.format(bucketname))
    for file in response['Contents']:
        filename = file['Key']

        copy_to_destination(filename)
        delete_from_Source(filename)

if __name__ == '__main__':
    main()


