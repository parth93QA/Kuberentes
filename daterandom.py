import datetime
import random


for i in range(0,3796):

    start_date = datetime.date(2001, 1, 1)
    end_date = datetime.date(2020, 12, 31)





    time_between_dates = end_date - start_date

    days_between_dates = time_between_dates.days

    random_number_of_days = random.randrange(days_between_dates)

    random_date = start_date + datetime.timedelta(days=random_number_of_days)

    print(random_date)



