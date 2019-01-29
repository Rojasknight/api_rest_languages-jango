import requests

headers = {}


headers['Authorization'] = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTQ4NzgzNzM0LCJqdGkiOiI0YmQyYmMyZTJlMTg0N2JlYTRiMWY1OTMyYzg0YTIzMiIsInVzZXJfaWQiOjF9.i-BSek6hNNjx8NoWQlKGYPl0U5ec1fTxX8aAx1F51zs'

r = requests.get('http://127.0.0.1:8080/paradigm/', headers=headers)
print(r.text)