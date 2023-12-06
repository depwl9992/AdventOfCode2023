from re import findall
# import urllib.request

nums = []

# for line in urllib.request.urlopen("https://adventofcode.com/2023/day/1/input").read():
num_dict = {
	"one": 1,
	"eno": 1,
	"two": 2,
	"owt": 2,
	"three": 3,
	"eerht": 3,
	"four": 4,
	"ruof": 4,
	"five": 5,
	"evif": 5,
	"six": 6,
	"xis": 6,
	"seven": 7,
	"neves": 7,
	"eight": 8,
	"thgie": 8,
	"nine": 9,
	"enin": 9
}

file1 = open("day1input.txt","r")
cal_value = 0
match_str = "(\d|one|eno|two|owt|three|eerht|four|ruof|five|evif|six|xis|seven|neves|eight|thgie|nine|enin)"
for line in file1.readlines():
	print("\n ..Searching " + line + " for the calibration value...")
	search2 = findall(r"^.*" + match_str + "",line)
	search1 = findall(r"" + match_str + ".*$",line)
	if (not search1 or len(search1) == 0) and (not search2 or len(search2) == 0):
		print(" ..There were no calibration codes found in that text.")
	else:
		first_num = search1[0]
		last_num = search2[0]
#		print(first_num + " and " + last_num)
		if not first_num.isnumeric():
			first_num = num_dict[first_num]
		
		if not last_num.isnumeric():
			last_num = num_dict[last_num]
		
		nums.append(int(str(first_num) + str(last_num)))
#		print(" ..Found and stored " + str(nums[-1]) + " in calibration table.")		
#		print("Add " + str(nums[-1]) + " to " + str(cal_value) + " for " + str(cal_value + nums[-1]))
		cal_value += nums[-1]

print("\n\nWhat happy elves! The calibration value is calculated to be " + str(cal_value) + "!")