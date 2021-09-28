import requests 

city = input('Enter your surf city : ')
state = input('Enter State : ')

url = 'http://api.openweathermap.org/data/2.5/weather?q={},{}&appid=e0a83db3ba8fe4914daf6260ec80f58f&units=imperial'.format(city, state)

res = requests.get(url)
data = res.json()

weather = data['weather'][0]['description']
temp = data['main']['temp']
wind = data['wind']['speed']

print('======================================')
print('Weather: {}'.format(weather))
print('Temperature: {} degress fahrenheit'.format(temp))
print('Wind Speed: {} mph'.format(wind))
print('======================================')