def student_marks_analysis():
    print("=== Student Marks Analysis Tool ===")
    marks = []
    
    # Accept 10 student marks
    for i in range(1, 11):
        while True:
            try:
                mark = float(input(f"Enter mark for student {i}: "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Error: Mark should be between 0 and 100.")
            except ValueError:
                print("Error: Please enter a valid numerical value.")
    
    # Calculations
    total_marks = sum(marks)
    average_mark = total_marks / len(marks)
    highest_mark = max(marks)
    lowest_mark = min(marks)
    
    # Display results
    print("\n--- Summary Report ---")
    print(f"Total Marks:   {total_marks:.2f}")
    print(f"Average Mark:  {average_mark:.2f}")
    print(f"Highest Mark:  {highest_mark:.2f}")
    print(f"Lowest Mark:   {lowest_mark:.2f}")

if __name__ == "__main__":
    student_marks_analysis()
