import boto3

def main():
    db_client = boto3.client('dynamodb', endpoint_url='http://localhost:8001')

    res=db_client.create_table(
    AttributeDefinitions=[
        {
            'AttributeName': 'id',
            'AttributeType': 'S',
        },
    ],
    KeySchema=[
        {
            'AttributeName': 'id',
            'KeyType': 'HASH',
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 1,
        'WriteCapacityUnits': 1,
    },
    TableName='board-mern',
)


    print("table created")

if __name__ == '__main__':
    main()