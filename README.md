Weather Man
the lab repo contains weather files for Murree. Write an application that generates the following reports. The user can specify more than one report at the same time. You have 3 days to submit
the first iteration from the day you are assigned this task.
The program should be designed as follows:
1. Define a data structure for holding each weather reading.
2. Define a class for parsing the files and populating the readings data structure with correct data types.
3. Define a data structure for holding the calculations results.
4. Define a class for computing the calculations given the readings data structure.
5. Define a class for creating the reports given the results data structure.
6. Define main for assembling the above and running the program.
7. Pep-8 conventions should be followed in the code.
1. For a given year display the highest temperature and day, lowest temperature and day, most humid day and humidity.
weatherman.py /path/to/files-dir -e 2002
Highest: 45C on June 23
Lowest: 01C on December 22
Humidity: 95% on August 14
2. For a given month display the average highest temperature, average lowest temperature, average mean humidity.
weatherman.py /path/to/files-dir -a 2005/6
Highest Average: 39C
Lowest Average: 18C
Average Mean Humidity: 71%
3. For a given month draw two horizontal bar charts on the console for the highest and lowest temperature on each day. Highest in red and lowest in blue.
weatherman.py /path/to/files-dir -c 2011/03
March 2011
01 +++++++++++++++++++++++++ 25C
01 +++++++++++ 11C
02 ++++++++++++++++++++++ 22C
02 ++++++++ 08C
4. Multiple Reports
weatherman.py /path/to/files-dir -c 2011/03 -a 2011/3 -e 2011
5. BONUS TASK. For a given month draw one horizontal bar chart on the console for the highest and lowest temperature on each day. Highest in red and lowest in blue.
weatherman.py /path/to/files-dir -c 2011/3
March 2011
01 ++++++++++++++++++++++++++++++++++++ 11C - 25C
02 ++++++++++++++++++++++++++++++ 08C - 22C
March 2011
01 ++++++++++++++++++++++++++++++++++++ 11C - 25C
02 ++++++++++++++++++++++++++++++ 08C - 22C
