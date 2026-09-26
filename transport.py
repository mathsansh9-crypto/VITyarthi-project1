def calculate_transport_emissions():
    print("\n--- Transport Emission Tracker ---")
    
    car_km = int(input("Enter weekly car distance (in km):"))
    print("Choose fuel type: 1. Petrol  2. Diesel  3. Electric 4. Hybrid")
    fuel_choice = input("Enter choice (1-4): ")
    
    if fuel_choice == "1":
        car_factor = 0.30  
    elif fuel_choice == "2":
        car_factor = 0.35
    elif fuel_choice == "3":
        car_factor = 0.10  
    else:
        car_factor = 0.20
    
        
    car_emission = car_km * car_factor

    transit_emission = float(input("Enter weekly public transit distance (in km): "))
    transit_emissions = transit_emission * 0.17

    flight_hours = float(input("Enter total flight hours taken this month: "))
    flight_emissions = (flight_hours * 90) / 4 

    total_transport = car_emission + transit_emissions + flight_emissions
    return total_transport