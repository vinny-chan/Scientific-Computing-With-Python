from helpers import add_day_of_week, get_military_time, get_period, get_days_later_description, get_twelve_hour_clock_time, get_hour_to_display, get_minute_to_display
from constants import SEMI_COLON, TIME_INDEX, PERIOD_INDEX, HOUR_INDEX, MINUTE_INDEX, MINUTES_IN_HOUR, HOURS_IN_DAY

def add_time(start, duration, dayOfWeek = ""):
  s = start.split()
  startTime = s[TIME_INDEX]
  t = startTime.split(SEMI_COLON)
  startHour = int(t[HOUR_INDEX])
  startMinute = int(t[MINUTE_INDEX])
  startPeriod = s[PERIOD_INDEX]
  startHour = get_military_time(startHour, startPeriod)

  d = duration.split(SEMI_COLON)
  durationHour = int(d[HOUR_INDEX])
  durationMinute = int(d[MINUTE_INDEX])

  totalMinutes = startMinute + durationMinute
  nextMinute = totalMinutes % MINUTES_IN_HOUR
  minuteCarryOver = totalMinutes // MINUTES_IN_HOUR

  nextHour = startHour + durationHour + minuteCarryOver
  nextPeriod = get_period(nextHour)
  daysLater = nextHour // HOURS_IN_DAY
  daysLaterDescription = get_days_later_description(daysLater)

  if dayOfWeek:
    dayOfWeek = ", " + add_day_of_week(dayOfWeek, daysLater)

  nextHour = get_twelve_hour_clock_time(nextHour)

  return get_hour_to_display(nextHour) + SEMI_COLON + get_minute_to_display(nextMinute) + " " + nextPeriod + dayOfWeek + daysLaterDescription