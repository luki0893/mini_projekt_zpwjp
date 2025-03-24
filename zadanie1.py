class Time:

    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    def __str__(self):
        return f"{self.hour}:{self.minute:02}"

    def time_validation(self):
        return 0 <= self.hour < 24 and 0 < self.minute <= 60

    def time_addition(self, other):
        total_minutes = self.minute + other.minute
        total_hours = self.hour + other.hour + (total_minutes // 60)
        total_minutes = total_minutes % 60
        total_hours = total_hours % 24
        return Time(total_hours, total_minutes)

    def __lt__(self, other):
        if isinstance(other, Time):
            return (self.hour, self.minute) < (other.hour, other.minute)



t1 = Time(13, 43)
t2 = Time(5, 22 )
t3 = Time(7, 33)
print(t1)
print(t2)

print(t1.time_validation())
print(t2.time_validation())
print("____________")
print(t1.time_addition(t2))

times = [t1, t2, t3]
sorted_times = sorted(times)
print("____________")
for t in sorted_times:
    print(t)

