import sys
import boto3

def main():
    s3 = boto3.resource("s3")
    #bucket name and file name
    bucket_name = sys.argv[1]
    object_name = sys.argv[2]

    try:
        response = s3.Object(bucket_name, object_name).put(Body=open(object_name, 'rb'))
        print response
    except Exception as error:
        print error

if __name__ == '__main__':
    main()