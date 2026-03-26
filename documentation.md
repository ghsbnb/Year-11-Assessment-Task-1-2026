## Requirements Definition

# This particular NSW weather app must have the ability to lidt the available cities, pull their geographical data, pull their weather data and display that information to the user clearly and efficiently.

## Functional specifications

# There are 3 key functional specifications:
# 1. The input and output of listing cities where the user needs to press 1
# 2. The input and output of grabbing city wweather data where the user will press 2 then type one of the listed cities.
# 3. The function to exit the program where the user presses 3 and the program prints "Goodbye!"
# These functions are diplayed in this code:
if choice == "1":
            list_cities()
        elif choice == "2":
            weather_for_city()
        elif choice == "3":
            print("Goodbye!")
            break

# Data Dictionary:

Variable   | Variable Type | Info
City       |  String       |   Location.
Temperature|  Float        |   The degrees celsius of the area.
Windspeed  |  Float        |   The speed of the wind in the city.

# Structure Chart

1. Start Menu 
Options:
1>Lists Cities
2>Prompts Input to enter city and then pulls information from api.
3>Exits and prints "Goodbye!".

# Pseudocode

got u:

import weatherapperror formatweatheroutput getcitycoordinates getnswcities getweather from functions
start showmenu
display nsw weather app
display 1 list nsw cities
display 2 get weather for a city
display 3 exit
end showmenu

begin promptchoice
ask user choose an option (1-3):
store input in choice
return choice trimmed
end promptchoice

begin listcities
set cities to getnswcities()
display nsw cities:
for each city in cities starting index at 1
display index + city
end for
end listcities

begin weatherforcity
ask user enter city name:
store input in city
trim city
if city is empty then
display city name is required
return
end if
try
set location to getcitycoordinates(city)
set weather to getweather(location latitude location longitude)
display formatweatheroutput(location weather)
catch weatherapperror
display error + message
catch anything
display unexpected error + message
end try
end weatherforcity

begin main
repeat forever
call showmenu
set choice to promptchoice()
if choice = 1 then
call listcities
else if choice = 2 then
call weatherforcity
else if choice = 3 then
display goodbye
stop loop
else
display invalid choice just use 1 2 or 3
end if
end repeat
end main

call main

# FlowChart

[ start ]
    ↓
[ show menu ]
    ↓
[ get user choice ]
    ↓
┌───────────────┐
│ choice = 1 ?  │
└───────┬───────┘
        │yes
        ↓
[ list cities ]
        ↓
      (loop back to menu)

        │no
        ↓
┌───────────────┐
│ choice = 2 ?  │
└───────┬───────┘
        │yes
        ↓
[ ask for city name ]
        ↓
┌──────────────────────┐
│ city empty?          │
└───────┬──────────────┘
        │yes
        ↓
[ show "city required" ]
        ↓
      (loop back)

        │no
        ↓
[ get coordinates ]
        ↓
[ get weather ]
        ↓
[ display formatted weather ]
        ↓
      (loop back to menu)

        │no
        ↓
┌───────────────┐
│ choice = 3 ?  │
└───────┬───────┘
        │yes
        ↓
[ display goodbye ]
        ↓
[ end ]

        │no
        ↓
[ invalid choice message ]
        ↓
      (loop back to menu)
