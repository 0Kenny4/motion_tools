# Speed Calculator, Mercer Kenyon, 4/9/2021, 1:46 pm v0.0

keep_going = "yes"

while keep_going == "Yes" or keep_going == "yes":

    distance = float(input("Please enter the distance and press enter.\n"))
    time = float(input("Please enter the time and press enter.\n"))

    speed = distance / time

    print(f"Using the distance of {distance} meters and time {time} seconds, the speed is m/s .\n")

    keep_going = input("Would you like to do another calculation? Type yes or no and press enter.\n")

print("Thank you for using this calculator.\n")