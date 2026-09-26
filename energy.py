def calculate_energy_emissions():
    print("\n--- Household Energy Tracker ---")
    
    electricity_kwh = float(input("Enter monthly electricity consumption (in kWh): "))

    gas_kwh = float(input("Enter monthly gas consumption (in kWh): "))
    
    elec_emissions_monthly = electricity_kwh * 0.85
    gas_emissions_monthly = gas_kwh * 0.20
    
    total_monthly = elec_emissions_monthly + gas_emissions_monthly
    
    weekly_energy_emissions = total_monthly / 4
    return weekly_energy_emissions