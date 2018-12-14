import boto3

def main():
    rds = boto3.client('rds')
    try:
    # get all of the db instances
        dbs = rds.describe_db_instances()
    for db in dbs['DBInstances']:
        print ("%s@%s:%s %s") % (
                db['MasterUsername'],
                db['Endpoint']['Address'],
                db['Endpoint']['Port'],
                db['DBInstanceStatus'])
    except Exception as error:
        print error


if __name__ == '__main__':
    main()