import os
import csv
import argparse


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
                            clean_row.get("PKT", ""),
                            clean_row.get("Max TemperatureC", ""),
                            clean_row.get("Min TemperatureC", ""),
                            clean_row.get("Max Humidity", "")
                        )
                        if reading.date:
                            weather_data.append(reading)
                    except Exception as e:
                        print(f"Error Processing Row: {e}")
                        continue
    return weather_data


def extreme_weather(weather_data, year):
    filter_data = []
    for reading in weather_data:
        if not reading.date:
            continue
        parts = reading.date.split("-")
        data_year = int(parts[0])
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
    print("Year Record")
    print(f"Highest Temperature is  {highest_temp}C on {highest_temp_date}")
    print(f"Lowest Temperature is  {lowest_temp}C on {lowest_temp_date}")
    print(f"Highest Humidity  is  {highest_humidity} on {highest_humidity_date}")


def month_weather(weather_data, year, month):
    month_data = []
    for reading in weather_data:
        if not reading.date:
            continue
        parts = reading.date.split("-")
        data_year = int(parts[0])
        data_month = int(parts[1])
        if data_year == year and data_month == month:
            month_data.append(reading)
    if not month_data:
        print("No record found")
        return
    max_temp = []
    min_temp = []
    humidity = []
    for reading in month_data:
        if reading.max_temp is not None:
            max_temp.append(reading.max_temp)
        if reading.min_temp is not None:
            min_temp.append(reading.min_temp)
        if reading.humidity is not None:
            humidity.append(reading.humidity)
    avg_max = sum(max_temp) / len(max_temp) if max_temp else None
    avg_min = sum(min_temp) / len(min_temp) if min_temp else None
    avg_humidity = sum(humidity) / len(humidity) if humidity else None
    print("Average Month Record")
    print(f"Highest Average Temperature: {round(avg_max, 1)}C")
    print(f"Lowest Average Temperature: {round(avg_min, 1)}C")
    print(f"Average Mean Humidity: {round(avg_humidity, 1)}%")


def graph_weather(weather_data, year, month):
    month_data = []
    for reading in weather_data:
        if not reading.date:
            continue
        parts = reading.date.split("-")
        data_year = int(parts[0])
        data_month = int(parts[1])
        if data_year == year and data_month == month:
            month_data.append(reading)
    if not month_data:
        print("No record found")
        return
    for reading in month_data:
        parts = reading.date.split("-")
        day = parts[2]
        max_line = ""
        min_line = ""
        if reading.max_temp is not None:
            max_line = "+" * reading.max_temp
        if reading.min_temp is not None:
            min_line = "-" * reading.min_temp
        print(f"{day} {max_line} {reading.max_temp}C")
        print(f"{day} {min_line} {reading.min_temp}C")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("folder")
    parser.add_argument("--yearly_report")
    parser.add_argument("--monthly_report")
    parser.add_argument("--bar_chart")
    args = parser.parse_args()
    weather_data = _weather_data(args.folder)
    if args.yearly_report:
        extreme_weather(weather_data, int(args.yearly_report))
    if args.monthly_report:
        parts = args.monthly_report.split("/")
        if len(parts) != 2:
            print("Invalid format ")
        else:
            try:
                year = int(parts[0])
                month = int(parts[1])
                month_weather(weather_data, year, month)
            except ValueError:
                print("Invalid format ")
    if args.bar_chart:
        parts = args.bar_chart.split("/")
        if len(parts) != 2:
            print("Invalid format ")
        else:
            try:
                year = int(parts[0])
                month = int(parts[1])
                graph_weather(weather_data, year, month)
            except ValueError:
                print("Invalid format ")


if __name__ == "__main__":
    main()
