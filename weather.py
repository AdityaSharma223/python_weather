import python_weather
import asyncio
CityName = "New Delhi"

async def getweather():
    # our list for storing the weather for the next few days
    a = []

    # declare the client. format defaults to the metric system (celcius, km/h, etc.)
    client = python_weather.Client(format=python_weather.METRIC)

    # fetch a weather forecast from a city
    weather = await client.find("{}".format(CityName))

    # get the weather forecast for a few days
    for forecast in weather.forecasts:
        a.append([str(forecast.date), forecast.sky_text, forecast.temperature])

    for i in a:
        print(i, end="\n")
    # close the wrapper once done
    await client.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(getweather())
