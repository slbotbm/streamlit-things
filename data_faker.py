import random
import pandas as pd
from faker import Faker
from datetime import datetime, timedelta


def important_task_maker(number):
    data = []
    for i in range(number):
        num = random.randint(1, number + 1)
        while num in data:
            num = random.randint(1, number + 1)
        data.append(num)
    return data


def dates_creator(number):
    data = []
    for i in range(number):
        created_at = datetime.now() - timedelta(days=random.randint(0, 365))
        updated_at = created_at + timedelta(days=random.randint(1, 365))
        time_limit = updated_at + timedelta(days=random.randint(180, 730))
        data.append([created_at, updated_at, time_limit])
    return data


number_of_items = 300
fake = Faker("ja_JP")
dates = dates_creator(number_of_items)
data = {
    "name": [fake.sentence() for _ in range(number_of_items)],
    "details": [fake.text() for _ in range(number_of_items)],
    "time_limit": [dates[i][2].strftime("%Y-%m-%d") for i in range(number_of_items)],
    "importance": important_task_maker(number_of_items),
    "cost": [random.randint(1000, 100000) for _ in range(number_of_items)],
    "category": [
        random.choice(["仕事", "運動", "家族", "友達"]) for _ in range(number_of_items)
    ],
    "complete": [random.choice([0, 1]) for _ in range(number_of_items)],
    "created_at": [dates[i][0].strftime("%Y-%m-%d") for i in range(number_of_items)],
    "updated_at": [dates[i][1].strftime("%Y-%m-%d") for i in range(number_of_items)],
}

df = pd.DataFrame(data)
df.to_csv("tasks_data.csv", index=False)
