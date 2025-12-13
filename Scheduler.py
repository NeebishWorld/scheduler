import pandas as pd

days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
periods = [
    "1 (09:00-09:45)",
    "2 (09:50-10:35)",
    "3 (10:40-11:25)",
    "4 (11:30-12:15)",
    "Lunch",
    "5 (13:00-13:45)",
    "6 (13:50-14:35)",
    "7 (14:40-15:25)",
    "8 (15:30-16:15)",
]

df = pd.DataFrame("", index=periods, columns=days)





df.loc["1 (09:00-09:45)", "Mon"] = "Alg2-A (Adam)"
df.loc["1 (09:00-09:45)", "Wed"] = "Alg2-A (Adam)"

print(df)
df = df.fillna("")  # NaN -> 빈칸

df.to_csv("schedule_candidate_1.csv", index_label="Time")
