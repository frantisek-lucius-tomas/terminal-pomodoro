import time

pomo_duration = int(input("how long do you want do pomodoro : ")) * 60
break_duration = int(input("and how long do you want the break to be : ")) * 60

for count in range(pomo_duration, 0, -1):

    seconds = count % 60
    minutes = int(count / 60) % 60

    print(f"\r{minutes:02}:{seconds:02}", end='')

    time.sleep(1)

for count in range(break_duration, 0, -1):

    seconds = count % 60
    minutes = int(count / 60) % 60

    print(f"\r{minutes:02}:{seconds:02}", end='')

    time.sleep(1)


print("\npomodoro and break are over, restart and go study again bitch")
