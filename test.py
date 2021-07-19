import requests

skill = 'JavaScript'

response = requests.get('https://google.com.br/')
print(response.status_code)

# response = requests.get('http://localhost:5000/skills/')
# print(response.json(), response.status_code)

# response = requests.post('http://localhost:5000/skills/', json=skill)
# print(response.json(), response.status_code)

# response = requests.put('http://localhost:5000/skills/0/', json='C++')
# print(response.json(), response.status_code)

# response = requests.delete('http://localhost:5000/skills/0/')
# print(response.json(), response.status_code)
