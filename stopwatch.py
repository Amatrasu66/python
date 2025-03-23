import time

time_showase = int(input("enter the time in seconds : "))

for i in range(time_showase,0,-1):
    seconds = i % 60
    minutes = (i // 60)% 60
    hours = i // 3600

    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("time's up buddy")
