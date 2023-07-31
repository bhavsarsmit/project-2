import requests #we need to import requests otherwise it will not work.
api_key='ed40a3091796e2917356c15cc7596cd7' #we need the api key to fetch a data, so i entered the API key from open weathermap.
#user_input=input("enter city: ")
city_name=input("Enter City Name: ")# user enter a city name, which one he wanted to check, so we take the input from user.
weather_data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city_name+"&appid=e39e9dd4ecaab22e3b5740766a953efc")
print(weather_data.status_code);
if(weather_data.status_code>=300): #this condition for, when the user will get any type off error, that's why.if output is above 300 it's concidered by error.
    data = weather_data.json();
    msg = data["message"];
    print(msg);
else:           #when output is ==200, user will geting the output as per his need,(successfull)
    data = weather_data.json();
    temperture = data["main"]["temp"]-273.15; #we will convert data in temprature.
    # print(temperture);
    tp="{:.2F}".format(temperture)
    print(tp)
#print(weather_data["main"]["temp"]-273.15);



