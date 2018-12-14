import boto3

def main():
   s3 = boto3.resource('s3')
   for bucket in s3.buckets.all():
       print (bucket.name)
       print ("---")
       for item in bucket.objects.all():
           print ("\t%s" %item.key)


if __name__ == '__main__':
    main()