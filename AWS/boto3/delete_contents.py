import sys
import boto3
s3 = boto3.resource('s3')

#will delete all the objects in each bucket passed in as an argument
for bucket_name in sys.argv[1:]:
    bucket = s3.Bucket(bucket_name)
    for key in bucket.objects.all():
        try:
            response = key.delete()
            print response
        except Exception as error:
            print error


if __name__ == '__main__':
    main()