def temperature_monitoring():
    print("=== Temperature Monitoring System (3D Array) Tool ===")
    
    # Structure: 7 days, 3 times, 2 rooms
    # temps[day][time][room]
    num_days = 7
    num_times = 3
    num_rooms = 2
    
    temps = []
    
    # Input Data
    # To keep the test short for the user, I'll advise them we are using 7 days.
    # In a real scenario, we might use fewer days for testing.
    print(f"Recording data for {num_days} days, {num_times} times per day, in {num_rooms} rooms.")
    
    for d in range(num_days):
        print(f"\nDay {d+1}:")
        day_temps = []
        for t in range(num_times):
            time_label = "Morning" if t == 0 else "Afternoon" if t == 1 else "Evening"
            print(f"  Time: {time_label}")
            time_temps = []
            for r in range(num_rooms):
                while True:
                    try:
                        temp = float(input(f"    Room {r+1} Temperature (°C): "))
                        time_temps.append(temp)
                        break
                    except ValueError:
                        print("      Error: Invalid temperature.")
            day_temps.append(time_temps)
        temps.append(day_temps)

    # Calculate Highest and Lowest
    highest_temp = -float('inf')
    lowest_temp = float('inf')
    
    for d in range(num_days):
        for t in range(num_times):
            for r in range(num_rooms):
                current_temp = temps[d][t][r]
                if current_temp > highest_temp:
                    highest_temp = current_temp
                if current_temp < lowest_temp:
                    lowest_temp = current_temp

    # Display results
    print("\n--- Temperature Summary ---")
    print(f"Highest Recorded Temperature: {highest_temp:.2f}°C")
    print(f"Lowest Recorded Temperature:  {lowest_temp:.2f}°C")

if __name__ == "__main__":
    temperature_monitoring()
