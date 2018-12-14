import boto3

def main():
  ec2 = boto3.resource('ec2')
  instance = ec2.create_instances(
    ImageId = 'ami-97785bed',
    MinCount = 1,
    MaxCount = 1,
    InstanceType='t2.micro')
  print (instance[0].id)

if __name__ == '__main__':
  main()
