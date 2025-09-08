import os, csv, argparse
class WeatherMan:
    def __init__(self, date, max_temp, min_temp, humidity):
        self.date = date
        try:
            self.max_temp = int(max_temp) if max_temp else None
        except ValueError:
            self.max_temp = None
        try:
            self.min_temp = int(min_temp) if min_temp else None
        except ValueError:
            self.min_temp = None
        try:
            self.humidity = int(humidity) if humidity else None
        except ValueError:
            self.humidity = None
def _weather_data(folder):
    weather_data = []
    for files in os.listdir(folder):
        if files.endswith(".txt"):
            with open(os.path.join(folder, files), "r") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    clean_row = {k.strip(): v.strip() for k, v in row.items()}
                    try:
                        reading = WeatherMan(
                            row.get("PKT", ""),
                            row.get("Max TemperatureC", ""),
                            row.get("Min TemperatureC", ""),
                            row.get("Max Humidity", "")
                        )
                        if reading.date:
                            weather_data.append(reading)
                    except Exception as e:
                        print(f"Error Processing Row: {e}")
                        continue
    return weather_data
def extreme_weather(weather_data,year):
    filter_data=[]
    for reading in weather_data:
        if not reading.date:
            continue
        parts = reading.date.split("-")
        data_year=int(parts[0])
        if data_year == year:
            filter_data.append(reading)
    if not filter_data:
        print(f"No record found for year {year}. Available data is only between 2004–2016.")
        return
    highest_temp = None
    highest_temp_date = None
    lowest_temp = None
    lowest_temp_date = None
    highest_humidity = None
    highest_humidity_date = None
    for reading in filter_data:
        if reading.max_temp is not None:
            if highest_temp is None or reading.max_temp > highest_temp:
                highest_temp = reading.max_temp
                highest_temp_date = reading.date
        if reading.min_temp is not None:
            if lowest_temp is None or reading.min_temp < lowest_temp:
                lowest_temp = reading.min_temp
                lowest_temp_date = reading.date
        if reading.humidity is not None:
            if highest_humidity is None or reading.humidity > highest_humidity:
                highest_humidity = reading.humidity
                highest_humidity_date = reading.date
    print(f"Highest Temperature is  {highest_temp}C on {highest_temp_date}")
    print(f"Lowest Temperature is  {lowest_temp}C on {lowest_temp_date}")
    print(f"Highest Humidity  is  {highest_humidity} on {highest_humidity_date}")

def main():
    parser = argparse.ArgumentParser(description="WeatherMan Reports")
    parser.add_argument("path", help="Path to weather files directory")
    parser.add_argument("-e", "--extreme", help="Report extreme values for a given year (e.g. 2005)")
    # later we will add -a and -c here
    args = parser.parse_args()

    weather_data = _weather_data(args.path)

    if args.extreme:
        extreme_weather(weather_data, int(args.extreme))
if __name__ == "__main__":
    main()



