# Carbon Footprint Tracker & Eco-Coach

A modular Python terminal application designed to track personal weekly carbon emissions across key lifestyle sectors—transportation, household energy usage, and dietary habits—and provide actionable, automated recommendations for reducing environmental impact.

## Table of Contents

* [Overview](#overview)

* [Features](#features)

* [Technologies & Tools Used](#technologies--tools-used)

* [Project Architecture](#project-architecture)

* [Steps to Install & Run](#steps-to-install--run)

* [Instructions for Testing](#instructions-for-testing)

* [Limitations](#limitations)

* [Future Improvements](#future-improvements)

## Overview

The **Carbon Footprint Tracker & Eco-Coach** helps individuals understand their personal environmental impact by converting daily routines and consumption data into measurable $CO_2$ equivalent emissions (in kilograms per week).

Based on input data across transport, utility usage, and dietary choices, the application evaluates total weekly emissions, assigns an ecological rating (e.g., *Eco Hero*, *Average Consumer*, *Needs Improvement*), and invokes an intelligent coaching module that identifies the user's single highest emission area to provide tailored reduction tips and weekly goals.

## Features

* **Interactive Emission Calculations**:

  * **Travel Emission Module (`transport.py`)**: Accounts for car mileage (factoring in petrol, diesel, electric, or hybrid engine types), public transit usage, and monthly flight history.

  * **Household Utility Module (`energy.py`)**: Converts monthly electricity (kWh) and gas (kWh) usage into weekly $CO_2$ metrics.

  * **Dietary Impact Module (`diet_impact.py`)**: Calculates food footprint based on diet style (Non-Vegetarian, Balanced, Vegetarian, Vegan) and local sourcing habits.

* **Eco Dashboard (`main.py`)**: Aggregates sector-wise emissions, displays total weekly footprint, and calculates an overall ecological performance rating.

* **Automated Recommendation System (`coach.py`)**: Dynamically identifies top emission drivers and offers targeted advice alongside an achievable 7% reduction goal.

* **Modular Design**: Clean separation of concerns with distinct Python modules for UI, data processing, and recommendation logic.

## Technologies & Tools Used

* **Programming Language**: Python 3.8+

* **Version Control**: Git & GitHub

* **Built-in Libraries**: Pure Python standard tools 

## Project Architecture

| **File** | **Module Name** | **Description** | 
| `main.py` | Eco Dashboard Core | Entry point of the program. Coordinates module workflows, computes total weekly footprint, and renders the user dashboard. | 

| `transport.py` | Travel Emission Module | Prompts for transport habits and calculates emissions based on fuel types and distance travelled. | 

| `energy.py` | Household Utility Module | Processes monthly electricity and gas consumption data into weekly CO2 values. | 

| `diet_impact.py` | Consumption Module | Evaluates dietary preferences and local sourcing choices to estimate food carbon costs. | 

| `coach.py` | Recommendation Module | Analyzes high-emission areas in user data and auto-generates custom eco-friendly habits. | 

## Steps to Install & Run

### Prerequisites

Make sure you have **Python 3.x** installed on your system. You can verify your installation by running:

```
python --version

```

or

```
python3 --version

```

### 1. Clone the Repository

Clone this repository to your local machine:

```
git clone https://github.com/mathsansh9-crypto/carbon-footprint-tracker.git
cd carbon-footprint-tracker

```

### 2. Run the Application

Execute the main entry script using Python:

```
python main.py

```

## Instructions for Testing

To test the application's functionality across various logic branches, follow these steps in your terminal:

1. **Launch the application**:

   ```
   python main.py
   
   ```

2. **Test Case 1: Low Impact User (Eco Hero)**

   * **Transport**: Car distance = `0`, Public transit = `10`, Flight hours = `0`

   * **Energy**: Electricity = `50` kWh, Gas = `20` kWh

   * **Diet**: Option `4` (Vegan), Local sourcing = `yes`

   * **Expected Output**: Rating should be `Excellent (Eco Hero)` (< 50kg co2/week)

3. **Test Case 2: High Impact User (Needs Improvement)**

   * **Transport**: Car distance = `300` (Petrol), Public transit = `50`, Flight hours = `10`

   * **Energy**: Electricity = `400` kWh, Gas = `200` kWh

   * **Diet**: Option `1` (Non-Vegetarian), Local sourcing = `no`

   * **Expected Output**: Rating should be `High Impact (Needs Improvement)` (>100kg co2/week) and `coach.py` should target the transport module.

4. **Test Case 3: Invalid Input Fallback**

   * In the Diet selection menu, enter an out-of-bounds choice like `99`.

   * **Expected Output**: Application should warn `"Invalid choice! Defaulting to Average diet."` and continue execution without crashing.

## Limitations

* **Static Conversion Factors**: Calculation multipliers (e.g., fuel factors, kWh to $CO_2$ ratios) are hardcoded estimates and do not account for regional power grid variations or real-time fuel efficiency differences.

* **Lack of Data Persistence**: Weekly calculation results are stored in-memory during execution and are lost once the program terminates.

* **CLI-Only Interface**: Currently operates entirely within a Command Line Interface (CLI), which may limit visual presentation and accessibility for non-technical users.

* **Basic Input Validation**: While default fallbacks exist for menu selections, some numeric inputs lack strict boundary and type validation checks.

## Future Improvements

* **Data Persistence & Analytics**: Integrate SQLite or JSON file storage to log historical weekly footprints and display progress trends over time.

* **Graphical User Interface (GUI)**: Develop a web dashboard (using Streamlit or Flask) or desktop GUI (Tkinter/PyQt) with visual charts and progress bars.

* **Regional & Dynamic Factors**: Incorporate APIs or region-specific lookup tables to retrieve dynamic carbon grid factors based on user location.

* **Expanded Emission Modules**: Add tracking for secondary consumption, such as shopping/waste, water usage, and digital carbon footprints.

* **Goal Progress Tracker**: Allow users to set personalized targets and track their progress toward achieving the 7% emission reduction goal.
