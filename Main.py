def print_stars():
    print("#"*30)


def print_current_attendance():
    print("Not Working")


def predict_attendance(current_percentage, next_working_days, desired_percentage):
    past_present_days = current_percentage * 100
    past_working_days = 100
    total_working_days = past_working_days + next_working_days

    number_of_days_required_to_meet_target = (
        (desired_percentage) * total_working_days) - past_present_days

    return number_of_days_required_to_meet_target


def Options():
    opt = ["Print Current Attendance", "Predict Attendance", ]
    for i in range(len(opt)):
        print(f"Enter {i+1} for {opt[i]}")

    Choice = int(input(":"))
    if Choice == 1:
        print_current_attendance()

    elif Choice == 2:
        current_percentage = float(input("Current attendance (in decimal) :"))
        next_working_days = int(input("For next how many work days :"))
        desired_percentage = float(input("Desired attendance (in decimal) :"))
        ans = predict_attendance(
            current_percentage, next_working_days, desired_percentage)

        print(
            f"We have to go {ans} days in next {next_working_days} to achieve {desired_percentage * 100 } Attendance.")


if __name__ == "__main__":
    print_stars()
    print("Attendance Management System \n")
    print_stars()

    Options()
