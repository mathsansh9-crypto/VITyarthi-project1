import transport
import energy
import diet_impact
import coach

def get_ecological_rating(total_emissions):
    if total_emissions < 50:
        return " Excellent (Eco Hero)"
    elif total_emissions <= 100:
        return " Moderate (Average Consumer)"
    else:
        return "High Impact (Needs Improvement)"

def main():
    print("==========================================")
    print("   CARBON FOOTPRINT TRACKER & ECO-COACH   ")
    print("==========================================")
    
    tem= transport.calculate_transport_emissions()
    eem = energy.calculate_energy_emissions()
    dem = diet_impact.calculate_diet_emissions()
    
    total_weekly_emissions = tem + eem + dem
    rating = get_ecological_rating(total_weekly_emissions)
    
    print("\n" + "="*40)
    print("             ECO DASHBOARD               ")
    print("="*40)
    print(f"Transport Emissions : {tem:.2f} kg CO2/week")
    print(f"Household Energy    : {eem:.2f} kg CO2/week")
    print(f"Diet Impact         : {dem:.2f} kg CO2/week")
    print("-" * 40)
    print(f"Total Footprint     : {total_weekly_emissions:.2f} kg CO2/week")
    print(f"Ecological Rating   : {rating}")
    
    coach.get_eco_recommendations(tem, eem, dem)

if __name__ == "__main__":
  main()
