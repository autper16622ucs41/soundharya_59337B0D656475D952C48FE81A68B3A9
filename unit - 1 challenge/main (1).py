def isLeapYear(year):
  if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    return True
  else:
    return False

year = 2040

if isLeapYear(year):
  print('{} is a Leap year.'.format(year))
else:
  print('{} is not a Leap year.'.format(year))