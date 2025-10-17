import requests

def get_data() -> dict:
    request = requests.get('https://jsonplaceholder.typicode.com/todos/1')
    data:dict=request.json()
    
    return data