# Carbon Footprint. Eco Coach

A Python terminal app that helps track personal weekly carbon emissions in important areas like transport home energy use and what people eat. It gives tips to help reduce the effect on the environment.

## Table of Contents

* [Overview](#overview)

* [Features](#features)

* [Technologies And Tools Used](#technologies--tools-used)

* [Project Architecture](#project-architecture)

* [Steps To Install And Run](#steps-to-install--run)

* [Instructions For Testing](#instructions-for-testing)

* [Limitations](#limitations)

* [Future Improvements](#future-improvements)

## Overview

The Carbon Footprint Tracker And Eco Coach helps people see how much they affect the environment by turning activities and what they use into numbers of CO2.

By looking at the data from transport, energy use and food choices the app finds the CO2 for the week. It gives a rating like Eco Hero, Average Consumer or Needs Improvement. Then it looks for the area with the emissions and offers tips to reduce it.

## Features

* Interactive Emission Calculations:

* Travel Emission Module (transport.py): Checks car use based on fuel type, public transport and flights.

* Household Utility Module (energy.py): Changes electricity and gas use into CO2 numbers each week.

* Dietary Impact Module (diet_impact.py): Figures out the carbon cost of food based on diet type and where it is bought.

* Eco Dashboard (main.py): Shows all the numbers from areas adds them up and gives a rating for how well someone is doing.

* Automated Recommendation System (coach.py): Finds the areas with high emissions and gives tips to help cut them. It also sets a goal to reduce by 7%.

* Modular Design: The app is split into parts so each part does its own job. There are parts for the display, calculations and recommendations.

## Technologies And Tools Used

* Programming Language: Python 3.8+

* Version Control: Git And GitHub

* Built-in Libraries: Python standard tools

## Project Architecture

| File | Module Name | Description |

| main.py | Eco Dashboard Core | Starts the program. Coordinates the parts calculates the total CO2 for the week and shows the results.

| Transport.py | Travel Emission Module | Asks about transport habits and calculates the emissions based on fuel type and distance. |

| Energy.py Household Utility Module | Changes electricity and gas use into weekly CO2 numbers.

| Diet_impact.py | Consumption Module | Looks at food choices and where food comes from to find the carbon cost.

| Coach.py | Recommendation Module | Checks the areas with the most emissions and gives tips to help reduce them. |

## Steps To Install And Run

### Prerequisites

Make sure Python 3.1+ is on your system. Check it by running:

```

python --version

```

or

```

python3 --version

```

### 1. Clone The Repository

Get this project to your computer:

```

git clone https://github.com/mathsansh9-crypto/carbon_footprint_tracker
cd carbon-footprint-tracker

```

### 2. Run The Application

Start the file with Python:

```

python main.py

```

## Instructions For Testing

To check if the app works in different situations follow these steps:

1. Start the app:

```

python main.py

```

2. Test Case 1: Low Impact User (Eco Hero)

* Transport: Car distance = 0 Public transit = 10 Flight hours = 0

* Energy: Electricity = 50 kWh, Gas = 20 kWh

* Diet: Choose 4 (Vegan) Local sourcing = yes

* Expected Result: Rating should be Eco Hero) (less than 50kg CO2 per week)

3. Test Case 2: High Impact User (Needs Improvement)

* Transport: Car distance = 300 (Petrol) transit = 50 Flight hours = 10

* Energy: Electricity = 400 kWh, Gas = 200 kWh

* Diet: Choose 1 (Non-Vegetarian) Local sourcing = no

* Expected Result: Rating should be High Impact (Needs Improvement) ( than 100kg CO2 per week) and coach.py should focus on transport.

4. Test Case 3: Invalid Input Fallback

* In the Diet selection put a choice like 99.

* Expected Result: The app should warn " choice! Defaulting to diet.". Keep running without errors.

## Limitations

* Static Conversion Factors: The numbers used for calculations like fuel amounts and kWh to CO2 are. Do not change for different places or real-time conditions.

* No Data Storage: The numbers for the week are kept in memory while the app is running and are lost once the program ends.

* Only Command Line: Works through the command line, which may not be easy for some people to use.

* Basic Checks: Some parts have checks for menu choices but other numbers do not have checks for correct values or types.

## Future Improvements

* Save Data And Analyze: Add a way to keep the numbers over time and show how they change.

* Better Interface: Make a web or desktop version with charts and easy to see progress.

* Use Data: Add ways to get live or local information to make the numbers more accurate.

* Add Areas: Track parts of life, like shopping, water use and how much the internet affects the environment.

* Track Goals: Let users set their targets and see how they do in reaching the 7% reduction goal.
