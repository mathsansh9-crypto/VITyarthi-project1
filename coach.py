def get_eco_recommendations(transport, energy, diet):
    print("\n" + "="*40)
    print("        ECO-COACH RECOMMENDATIONS        ")
    print("="*40)
    
    highest = max(transport, energy, diet)
    
    if highest == transport:
        print("Priority Area: Transport")
        print("- Try carpooling or using public transit twice a week.")
        print("- For short distances, walk or cycle instead of driving.")
    elif highest == energy:
        print("Priority Area: Household Energy")
        print("- Turn off lights and unplug electronics when not in use.")
        print("- Lower thermostat settings by 1-2 degrees in winter.")
    else:
        print("Priority Area: Diet")
        print("- Incorporate 2-3 meat-free days per week.")
        print("- Buy local, seasonal produce to reduce food transport impact.")

    print("\nWeekly Goal: Try to lower your total score by 7%next week!")