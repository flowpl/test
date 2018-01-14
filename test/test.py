from requests import get

result = get('https://google.de')
print(result.text)
print('another output')
print('another')

