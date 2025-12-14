import pandas as pd





days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
periods = [
    "09:00-09:45",
    "09:50-10:35",
    "10:40-11:25",
    "11:30-12:15",
    "LUNCH",
    "13:00-13:45",
    "13:50-14:35",
    "14:40-15:25",
    "15:30-16:15",
]

df = pd.DataFrame("", index=periods, columns=days)


# 여기서부 다시 시작하면 될듯.
teachers = [
  {"name":"Adam", "can_teach":["ALG2"], "avail":{"Mon":[(9,12.25),(13,16.25)], ...}},
]
subjects = [{"code":"ALG2", "meetings_per_week":5}]
students = [{"name":"S1", "required":["ALG2","ENG10"]}]


df.loc["09:00-09:45", "Mon"] = "Alg2-A (Adam)"
df.loc["09:00-09:45", "Wed"] = "Alg2-A (Adam)"

print(df)
df = df.fillna("")  # NaN -> 빈칸

df.to_csv("schedule_candidate_1.csv", index_label="Time")
