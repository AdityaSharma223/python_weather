import python_weather
import asyncio

async def getweather():
    # declare the client. format defaults to the metric system (celcius, km/h, etc.)
    client = python_weather.Client(format=python_weather.METRIC)

    # fetch a weather forecast from a city
    weather = await client.find("New Delhi")

    # returns the current day's forecast temperature (int)
    print(weather.current.temperature)
    a = []
    # get the weather forecast for a few days
    for forecast in weather.forecasts:
        a.append([str(forecast.date), forecast.sky_text, forecast.temperature])
    print(x for x in a)
    print(a)
    # close the wrapper once done
    await client.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(getweather())
