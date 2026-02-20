def student_score_table():
    print("=== Student Score Table Tool ===")
    
    num_students = 3
    num_subjects = 4
    # 2D array to store scores: scores[student][subject]
    scores = []
    
    # Input data
    for i in range(num_students):
        print(f"\nEntering scores for Student {i+1}:")
        student_scores = []
        for j in range(num_subjects):
            while True:
                try:
                    val = float(input(f"  Enter mark for Subject {j+1}: "))
                    student_scores.append(val)
                    break
                except ValueError:
                    print("  Error: Please enter a numeric value.")
        scores.append(student_scores)

    # Display Table Header
    print("\n" + "="*60)
    print(f"{'Student':<10} | {'S1':<6} | {'S2':<6} | {'S3':<6} | {'S4':<6} | {'Total':<8} | {'Avg':<6}")
    print("-" * 60)

    # Calculate and Display rows
    for i in range(num_students):
        student_row = scores[i]
        total = sum(student_row)
        avg = total / num_subjects
        
        print(f"Student {i+1:<2} | {student_row[0]:<6.1f} | {student_row[1]:<6.1f} | "
              f"{student_row[2]:<6.1f} | {student_row[3]:<6.1f} | {total:<8.1f} | {avg:<6.1f}")
    
    print("="*60)

if __name__ == "__main__":
    student_score_table()
