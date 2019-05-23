seconds = int(input("Enter seconds: "))
hours = seconds / 3600
remainder = seconds % 3600
minutes = remainder / 60
second = remainder % 60
print("Hours: %d" % hours)
print("Minutes: %d" % minutes)
print("Seconds: %d" % second)

future = int(input("How much do you want to have after 10 years: "))
present = future/(1 + .0299)**10
print("Invest: %.2f now" % present)
