INCREASING = 1
DECREASING = 2

f = open("../Inputs/day2_input.txt", "r")
unsplit_report_array = f.readlines()
f.close()

report_array = []

for report in unsplit_report_array:
    report_array += [report.split(' ')]

def go_through_report(report):
    up_or_down = 0
    failed = 0
    for i in range(1, len(report)):
        level = int(report[i])
        prev_level = int(report[i - 1])
        if abs(level - prev_level) < 1 or abs(level - prev_level) > 3: # Check for out-of-bound size increase/decrease
            failed = 1
            break
        if (level - prev_level) < 0:
            if up_or_down == INCREASING:
                failed = 1
                break
            up_or_down = DECREASING
        if (level - prev_level) > 0:
            if up_or_down == DECREASING:
                failed = 1
                break
            up_or_down = INCREASING
    if failed == 0:
        return True
    return False

safe_count = 0
for report in report_array:
    if go_through_report(report):
        safe_count += 1
    else: # God forgive me
        singlular_success = False
        for i in range(len(report)):
            singlular_success = go_through_report(report[:i] + report[i + 1:])
            if singlular_success:
                safe_count += 1
                break



print(safe_count)