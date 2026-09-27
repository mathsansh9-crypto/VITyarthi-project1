# Project Statement: Carbon Footprint Tracker & Eco‑Coach

## Problem Statement

Due to climate worries the Carbon Footprint Tracker & Eco‑Coach highlights the importance of individual contribution to the reduction of greenhouse gases. However, many people fail to see the connection between their day-to-day actions, such as transportation, electricity and gas consumption, and the diet they choose to follow, to a carbon footprint measured in CO2 emissions.

In addition, the standard environmental advice may appear vague or even counterproductive. Therefore, without the tool that identifies the user's current emission level and provides relevant local recommendations, it is challenging to recognize significant contributors to the global impact and track progress with precision.

## Scope of the Project

The Carbon Footprint Tracker & Eco‑Coach is a modular Python-based application designed for the terminal. It estimates an individual's carbon emissions in three key areas of human activity and offers targeted recommendations for reducing the impact.

### In Scope:

Transportation Emissions (`transport.py`):

Calculates the car emission, depending on the fuel used (Petrol, Diesel, Electric, Hybrid). Public Transport distance is added. Flights are estimated by the number of flights taken per week.

Household Utility Emissions (`energy.py`):

The electricity and gas consumption for a household for a specific period (in kWh) are converted to CO2 emissions for a week.

Dietary Footprint (`diet_impact.py`):

Based on the type of diet (Non‑Vegetarian, Balanced, Vegetarian, Vegan), the diet-related CO2 emissions are estimated. Farm to Fork initiative carbon‑offset is applied.

Dashboard & Rating Core (`main.py`):

The emissions in each area are summed up to a carbon footprint for a week in kg of CO2 and displayed as an Eco Hero, Average Consumer, or Needs Improvement rating.

Automated Eco‑Coach (`coach.py`):

The highest-ranking impact area is identified, a list of relevant solutions is provided, and a goal is set for the following week to reduce the overall carbon footprint by 7 %.

### Not In Scope For This Version:

Connecting to external APIs to provide the carbon footprint based on real-time grid electricity mix data.

A database to keep the user's footprint history between the software runs.

Graphic and Mobile UI.

## Target Users

1. Environmentally Conscious Individuals: To get a sense of their carbon footprint and participate in the environmental protection.

2. Academic: To evaluate the carbon footprint from a mathematical point of view.

3. Eco‑Friendly Beginners: To obtain a reliable coach, avoiding complicated environmental science jargon.

## High‑Level Features

Multi‑Factor Input Logic: The application asks for the input data in all three areas: transportation, electricity and gas, and diet.

Modular Codebase: The Carbon Footprint Tracker & Eco‑Coach software is separated into Python files for each of the three areas, plus the dashboard and the coach.

Instant Emission Analytics: The dashboard displays the user's overall carbon footprint in CO2 emissions and ranks it as an Eco Hero, Average Consumer, or Needs Improvement.

Targeted Coaching Algorithm: The highest impact area is detected and shown first; the solutions are easy to understand, relevant, and set a goal for the following week to reduce the carbon footprint by 7 %.
