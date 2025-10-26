import datetime as dt

date = dt.date(2025, 2, 14)
print(date)

today = dt.date.today()
print(today)

time = dt.time(12, 30, 0)
print("\n", time)

now = dt.datetime.now()
print(f" {now}")

now = now.strftime("%H:%M:%S %m-%d-%Y")
print(f" {now}")

print("\n\n")

target_datetime = dt.datetime(2030, 1, 20, 12, 30, 1)
current_datetime = dt.datetime.now()

if target_datetime < current_datetime:
    print("Target date has passed!")
else:
    print("Target date has NOT passed!")
    