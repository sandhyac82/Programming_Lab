import datetime
t=datetime.time(22,56,20,67)
print(t)
print("Hour",t.hour)
print("Minutes",t.minute)
print("Seconds",t.second)
print("Microsecond:",t.microsecond)

print("\n")
d=datetime.date.today()
print("Today:",d)
print("Year:",d.year)
print("Month:",d.month)
print("Day:",d.day)

d1=datetime.date.today()
print(d1)
td=datetime.timedelta(days=2)
print(td)
d2=d1+td
print(d2)

dt=datetime.datetime.combine(d1,t)
print("date-time comb:",dt)

