def calculate_diet_emissions():
    print("\n--- Diet Impact Tracker ---")
    print("Select primary diet type:")
    print("1. Non-Vegetarian / Meat Lover")
    print("2. Balanced / Average")
    print("3. Vegetarian")
    print("4. Vegan")
    
    choice = input("Enter choice (1-4): ")
    
    if choice == "1":
        base_emissions = 60 
    elif choice == "2":
        base_emissions = 45
    elif choice == "3":
        base_emissions = 30
    elif choice == "4":
        base_emissions = 20
    else:
        print("Invalid choice! Defaulting to Average diet.")
        base_emissions = 45

    local_sourced = input("Do you mostly buy locally sourced food? (yes/no): ").strip().lower()
    if local_sourced == "yes":
        base_emissions -= 5  
        
    return base_emissions