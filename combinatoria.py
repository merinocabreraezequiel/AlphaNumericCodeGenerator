import string
import time

def stepbystep(characters = [0,0,0,0,0,0,0,0,0,0,0,0]):
	lettersAndDigits = string.ascii_letters + string.digits
	return ''.join(lettersAndDigits[characters[letterPosition]] for letterPosition in range(12))

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
for a in range(62):
	for b in range(62):
		for c in range(62):
			for d in range(62):
				for e in range(62):
					for f in range(62):
						for g in range(62):
							for h in range(62):
								for i in range(62):
									for j in range(62):
										for k in range(62):
											for l in range(62):
												count += 1
												code = stepbystep([a,b,c,d,e,f,g,h,i,j,k,l])
												if (code.isdigit()):
													onlyDigit += 1
												if (count % 1000000 == 0):
													print (onlyDigit, "/", count, "(", dayshoursminutes(), ") -", code)
