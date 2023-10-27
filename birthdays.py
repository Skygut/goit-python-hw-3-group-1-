from datetime import datetime, date
from collections import defaultdict

users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 10, 16)},
    {"name": "Mark Koll", "birthday": datetime(1985, 10, 14)},
    {"name": "Marie Bauer", "birthday": datetime(1990, 10, 17)},
    {"name": "Alex Graf", "birthday": datetime(1978, 10, 19)},
]


def get_birthdays_per_week(users):
    current_date = datetime.today().date()
    list_birthdays_next_week = defaultdict(list)
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=current_date.year)
        delta_days = (birthday_this_year - current_date).days
        if delta_days < 7:
            day_of_week = user["birthday"].strftime("%A")
            if day_of_week == "Saturday" or day_of_week == "Sunday":
                list_birthdays_next_week["Monday"].append(name)
            else:
                list_birthdays_next_week[day_of_week].append(name)
    birthday_list = "\n".join(
        f"{day}: {', '.join(names)}" for day, names in list_birthdays_next_week.items()
    )

    return birthday_list


if __name__ == "__main__":
    print("Get birthdays for next 7 days!")
    print(get_birthdays_per_week(users))
