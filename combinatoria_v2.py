#Worst than the first
import string
import time

def dayshoursminutes():
	totalSeconds = round(time.time() - start_time)
	day = totalSeconds // (24 * 3600)
	totalSeconds = totalSeconds % (24 * 3600)
	hour = totalSeconds // 3600
	totalSeconds %= 3600
	minutes = totalSeconds // 60
	totalSeconds %= 60
	seconds = totalSeconds
	dhms = str(day) + ":" + str(hour) + ":" + str(minutes) + ":" + str(seconds)
	return (dhms)

start_time = time.time()
count=0
onlyDigit=0
lettersAndDigits = string.ascii_letters + string.digits
for a in lettersAndDigits:
	for b in lettersAndDigits:
		for c in lettersAndDigits:
			for d in lettersAndDigits:
				for e in lettersAndDigits:
					for f in lettersAndDigits:
						for g in lettersAndDigits:
							for h in lettersAndDigits:
								for i in lettersAndDigits:
									for j in lettersAndDigits:
										for k in lettersAndDigits:
											for l in lettersAndDigits:
												count += 1
												code = a+b+c+d+e+f+g+h+i+j+k+l
												if (code.isdigit()):
													onlyDigit += 1
												print (onlyDigit, "/", count, "(", dayshoursminutes(), ") -", code)
