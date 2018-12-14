import sys
import boto3

def main():
    db = sys.argv[1] #name of the instance to be deleted
    rds = boto3.client('rds')
    try:
        response = rds.delete_db_instance(
            DBInstanceIdentifier=db,
            SkipFinalSnapshot=True)
        print (response)
    except Exception as error:
        print (error)


if __name__ == '__main__':
    main()