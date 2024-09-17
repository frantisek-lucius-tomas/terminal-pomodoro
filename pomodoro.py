import time

duration = int(input())

for count in range(duration, 0, -1):

    seconds = count % 60
    minutes = int(count / 60) % 60
    hours = int(count / 3600)

    print(f"\r{hours:02}:{minutes:02}:{seconds:02}", end='')

    time.sleep(1)

print("\nend")
