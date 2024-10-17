# functions/hello.py
def handler(event, context):
    return {
        'statusCode': 200,
        'body': 'Hello from Python!'
    }
