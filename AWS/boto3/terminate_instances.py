import sys
import boto3

def main():
    ec2 = boto3.resource('ec2')
    for instance_id in sys.argv[1:]:
        response = ec2.instances.terminate(instance_id)
        print (response)


if __name__ == '__main__':
    main()