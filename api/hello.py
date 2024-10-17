# api/hello.py
def handler(request):
    return {
        'statusCode': 200,
        'body': 'Hello from Python!'
    }
