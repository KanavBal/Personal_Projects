import csv # Handling CSV files
import json # Handling JSON files
import os # Operating system functions
import re # Regular Expressions



class Exersise:
    def __init__(self, name, personalBest):
        self.name = name.strip()
        self.personalBest = personalBest

# This part checks if name is valid
    # Property for name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name") # Raises a valueerror
        if not re.fullmatch(r"^[A-Za-z0-9 -]+$", name):
                    raise ValueError("Invalid Input")
        self._name = name

class Workout:
    def __init__(self, date):
        self.date = date
        self.workout_log = []

    def assign_data(self, name, weight, reps):
        log = {
            "Name": name,
            "Weight": weight,
            "Reps": reps
        }

        self.workout_log.append(log)

    def to_dict(self): # Converts the data in object to dictionalry
        return {
            "Date": self.date,
            "Log": self.workout_log
        }


def main():

    exit = False
    while exit == False:
        load_exersises()

        print(f"Welcome to this fitness tracker. Please chose one of the following:")
        start = getint(f"1. Load a new exersise \n2. Create workout log \n3. See previous workouts\n4. Exit\n")
       
        match start:
            case 1:
                exersise = create_exersise()
                add_exersise(exersise.name, exersise.personalBest)
                exit = ask_exit()
                
            case 2:    
                current_workout = get_workout() # This creates an workout object type
                moreExersise = True
                while moreExersise == True:
                    print_exersise() # Loads a list of all the exersises in the memory
                    workout = getint("Choose the number of exersise: ")

                    exersise = get_exersise_number(workout) # Gets the name of exersise based on number
                    weight, reps = get_exersise() # Gets the reps and weight from user. 

                    current_workout.assign_data(exersise, weight, reps) # Assigns attributes to workout object

                    # Updating PR if neccesary:
                    pr = get_exerise_personalBest(workout) # Gets the PR based on the number of exersise
                    if weight > pr:
                        updatepb(exersise, weight)


                    if input(f"Do you want to contenue with the log? (y/n)\n") == "n":
                        moreExersise = False

                save_json(current_workout.to_dict()) # Saves the whole object to the json file

                exit = ask_exit()

            case 3:
                # Load JSON file containing workout logs
                with open("workouts.json", "r") as file:
                    workouts = json.load(file)

                # Print list of all workouts
                for number, workout in enumerate(workouts, start=1):
                    print(f"{number}. {workout['Date']}")
                    for exercise in workout["Log"]:
                        print(f"{exercise['Name']} - {exercise['Weight']} kg x {exercise['Reps']}")
                    print("\n")
                
                exit = ask_exit()

            case 4:
                exit = ask_exit()

            case _:
                print("Invalid Input, Try a number from the list.\n")



def get_exersise():
    reps = getint("Enter reps: ")
    weight = float(input("Enter weight: "))
    return weight, reps

def create_exersise():
    name = input(f"What is the name of the exersise: \n")
    personalBest = input("What is your PR : \n")
    return Exersise(name, personalBest)

def load_exersises():
    exersises = []
    with open("exersises.csv", "r") as file:
        reader = csv.DictReader(file)
        for line in reader:
            exersises.append(line["Name"])
    return exersises

def get_exersise_number(target_number):
    # Use the number of the exersise to get its name for the log
    with open("exersises.csv", "r") as file:
        reader = csv.DictReader(file)
        for number, line in enumerate(reader, start = 1):
            if number == int(target_number):
                return line["Name"]
    return None

def get_exerise_personalBest(target_number):
    # Use the number of the exersise to get its PR
        with open("exersises.csv", "r") as file:
            reader = csv.DictReader(file)
            for number, line in enumerate(reader, start = 1):
                if number == int(target_number):
                    return float(line["Personal Best"])
        return None

def updatepb(name, new_pr):
    exercises = []

    with open("exersises.csv", "r") as file:
        reader = csv.DictReader(file)

        for line in reader:
            if line["Name"] == name:
                line["Personal Best"] = new_pr

            exercises.append(line)

    with open("exersises.csv", "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["Name", "Personal Best"]
        )

        writer.writeheader()
        writer.writerows(exercises)

def add_exersise(name, personalBest):
    alreadyExersise = False
    # Checking if exerisise is already in the list
    with open("exersises.csv", "r") as file:
        reader = csv.DictReader(file)
        for number, line in enumerate(reader, start = 1):
            if name == line["Name"]:
                alreadyExersise = True
                        
        if alreadyExersise == False:
            print(f"{name} has now been added as a new exersise!")

            with open("exersises.csv", "a") as file:
                writer = csv.DictWriter(file, fieldnames=["Name", "Personal Best"])
                writer.writerow({"Name": name, "Personal Best": personalBest})
        else:
            print("Exersise is already loaded. Try again!")

def ask_exit():
    if input("Do you want to exit (y/n)?") == "y":
        return True
    else:
        return False

def getint(promt): # Validates if an input is valid
    while True:
        try:
            x = int(input(promt))
        except ValueError:
            print("Invalid Input, Try again.")
        else:
            return x

def get_workout():
    date = input("Enter the date of the workout: ")
    return Workout(date)

def save_json(log):
    try:
        with open("workouts.json", "r") as file:
            workouts = json.load(file)
    except FileNotFoundError:
        workouts = []
    
    workouts.append(log)
    
    with open("workouts.json", "w") as file:
        json.dump(workouts, file, indent=4)

def print_exersise():
    print(f"Here are the loaded exersises: ")
    with open("exersises.csv", "r") as file:
        reader = csv.DictReader(file)
        for number, line in enumerate(reader, start = 1):
            print(f"{number} {line["Name"]}")

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")

if __name__ == "__main__": # Only runs main function if the file is the primary code file. 
    main()