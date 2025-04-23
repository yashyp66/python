class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.normalize()

    def normalize(self):
        # Normalize seconds to minutes
        self.minutes += self.seconds // 60
        self.seconds = self.seconds % 60

        # Normalize minutes to hours
        self.hours += self.minutes // 60
        self.minutes = self.minutes % 60

    def display(self):
        print(f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}")

    def add(self, other):
        h = self.hours + other.hours
        m = self.minutes + other.minutes
        s = self.seconds + other.seconds
        return Time(h, m, s)

    def subtract(self, other):
        # Convert both times to total seconds
        t1_seconds = self.to_seconds()
        t2_seconds = other.to_seconds()
        diff = abs(t1_seconds - t2_seconds)
        return Time.from_seconds(diff)

    def to_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    @staticmethod
    def from_seconds(seconds):
        h = seconds // 3600
        m = (seconds % 3600) // 60
        s = seconds % 60
        return Time(h, m, s)

# Using the class
print("Enter first time:")
h1 = int(input("Hours: "))
m1 = int(input("Minutes: "))
s1 = int(input("Seconds: "))

print("\nEnter second time:")
h2 = int(input("Hours: "))
m2 = int(input("Minutes: "))
s2 = int(input("Seconds: "))

time1 = Time(h1, m1, s1)
time2 = Time(h2, m2, s2)

print("\nTime 1:")
time1.display()

print("Time 2:")
time2.display()

sum_time = time1.add(time2)
diff_time = time1.subtract(time2)

print("\nTime Addition:")
sum_time.display()

print("Time Difference:")
diff_time.display()
