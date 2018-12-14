import boto3

def main():
	ec2 = boto3.resource('ec2')
	for instance in ec2.instances.all():
		print (instance.id, instance.state)


if __name__ == '__main__':
	main()