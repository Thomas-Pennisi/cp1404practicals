"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Read subject data from file and display it"""
    subjects = load_subjects(FILENAME)
    display_subjects(subjects)

def load_subjects(filename=FILENAME):
    """Load data from file and format the code"""
    subject = []
    input_file = open(filename)
    for line in input_file:
        line = line.strip()
        parts = line.split(',')
        parts[2] = int(parts[2])
        subject.append(parts)
    input_file.close()
    return subject

def display_subjects(subjects):
    """Display the subject data"""
    for subject in subjects:
        print(f"{subject[0]} is taught by {subject[1]:12} and has {subject[2]:3} students")

main()