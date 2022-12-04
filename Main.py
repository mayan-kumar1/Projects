def print_stars():
    print("#"*30)


def desired_attendance_percentage(current_percentage, next_working_days, desired_percentage):
    past_present_days = current_percentage * 100
    past_working_days = 100
    total_working_days = past_working_days + next_working_days

    number_of_days_required_to_meet_target = (
        (desired_percentage) * total_working_days) - past_present_days

    return number_of_days_required_to_meet_target


def Get_Maximum_achievable_attendance(current_percentage, next_working_days):
    past_present_days = current_percentage * 100
    past_working_days = 100
    total_working_days = past_working_days + next_working_days
    Maximum_achievable_attendance = (
        past_present_days + next_working_days)/(total_working_days)

    return Maximum_achievable_attendance


def Options():
    opt = ["Get Desired Percentage", "Get Maximum achievable attendance"]
    for i in range(len(opt)):
        print(f"Enter {i+1} for {opt[i]}")

    Choice = int(input(":"))

    if Choice == 1:
        current_percentage = float(input("Current attendance (in decimal) :"))
        next_working_days = int(input("For next how many work days :"))
        desired_percentage = float(input("Desired attendance (in decimal) :"))
        ans = desired_attendance_percentage(
            current_percentage, next_working_days, desired_percentage)

        print(
            f"We have to go {ans} days in next {next_working_days} to achieve {desired_percentage * 100 } Attendance.")

    elif Choice == 2:
        print("----Max Percentage----")
        current_percentage = float(input("Current attendance (in decimal) :"))
        next_working_days = int(input("For next how many work days :"))

        ans = Get_Maximum_achievable_attendance(
            current_percentage, next_working_days)
        percentage = "{:.2f}".format(ans*100)
        print(
            f"\nif we go college everyday for the next {next_working_days},\nwe can achieve attendance percentage of : {percentage}")


if __name__ == "__main__":
    print_stars()
    print("Attendance Management System \n")
    print_stars()

    Options()
