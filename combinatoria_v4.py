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
a = 0
while a <= 61:
	b=0
	while b <= 61:
		c=0
		while c <= 61:
			d=0
			while d <= 61:
				e=0
				while e <= 61:
					f=0
					while f <= 61:
						g=0
						while g <= 61:
							h=0
							while h <= 61:
								i=0
								while i <= 61:
									j=0
									while j <= 61:
										k=0
										while k <= 61:
											l = 0
											while l <= 61:
												count += 1
												code = stepbystep([a,b,c,d,e,f,g,h,i,j,k,l])
												if (code.isdigit()):
													onlyDigit += 1
												print (onlyDigit, "/", count, "(", dayshoursminutes(), ") -", code)
												l += 1
											k += 1
										j += 1
									i += 1
								h += 1
							g += 1
						f += 1
					e += 1
				e += 1
			d += 1
		c += 1
	b += 1
a += 1