def school_data_analysis():
    print("=== School Data Analysis (3D Array) Tool ===")
    
    # Structure: 2 classes, 3 students, 2 subjects
    # marks[class][student][subject]
    num_classes = 2
    num_students = 3
    num_subjects = 2
    
    marks = []
    
    # Input Data
    for c in range(num_classes):
        print(f"\nEntering data for Class {c+1}:")
        class_marks = []
        for s in range(num_students):
            student_marks = []
            for sub in range(num_subjects):
                while True:
                    try:
                        mark = float(input(f"  Student {s+1}, Subject {sub+1} Mark: "))
                        student_marks.append(mark)
                        break
                    except ValueError:
                        print("    Error: Invalid mark.")
            class_marks.append(student_marks)
        marks.append(class_marks)

    # Calculations and Display
    print("\n--- PERFORMANCE REPORT ---")
    overall_total = 0
    total_elements = num_classes * num_students * num_subjects
    
    for c in range(num_classes):
        class_total = 0
        for s in range(num_students):
            class_total += sum(marks[c][s])
        
        class_avg = class_total / (num_students * num_subjects)
        overall_total += class_total
        print(f"Class {c+1} Average Mark: {class_avg:.2f}")
    
    overall_avg = overall_total / total_elements
    print(f"\nOverall School Average: {overall_avg:.2f}")

if __name__ == "__main__":
    school_data_analysis()
