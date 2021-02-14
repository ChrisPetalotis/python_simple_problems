def add_time(start, duration, day=None):
  days = [
    'monday', 
    'tuesday',
    'wednesday',
    'thursday',
    'friday',
    'saturday',
    'sunday']
  
  startHour, startMinutes = tuple(start.split(':'))
  startHour = int(startHour)
  dayPart = (startMinutes.split(' '))[1]
  if (dayPart.lower() == 'pm'):
    startHour += 12
  startMinutes =  int(startMinutes.split(' ')[0])
  
  durHour, durMinutes = tuple(duration.split(':'))
  durHour, durMinutes = int(durHour), int(durMinutes)

  resultDay = None

  resultMinutes = startMinutes + durMinutes
  hoursAfter = resultMinutes // 60
  resultMinutes = resultMinutes % 60
  
  resultHour = startHour + durHour + hoursAfter
  daysAfter = resultHour // 24
  resultHour = resultHour % 24

  if resultHour >= 12:
    if resultHour > 12:
      resultHour -= 12
    dayPart = 'PM'
  else:
    if resultHour == 0:
      resultHour = 12
    dayPart = 'AM'

  new_time = ':'.join([str(resultHour), (str(resultMinutes).zfill(2) + ' ' + dayPart)])

  if day:
    resultDay = (days.index(day.lower()) + daysAfter) % 7
    new_time += ', ' + days[resultDay].capitalize()
  
  if daysAfter == 1:
    new_time += ' (next day)'
  elif daysAfter > 1:
    new_time += ' (' + str(daysAfter) + ' days later)'

  return new_time