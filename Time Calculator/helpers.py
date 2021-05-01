from constants import DAY_OF_WEEK, MORNING, AFTERNOON, HOURS_IN_DAY, HOURS_IN_PERIOD, HOURS_IN_DAY, HOURS_IN_PERIOD

def add_day_of_week(start, duration):
  day = DAY_OF_WEEK[start.lower()]
  nextDayOfWeek = (day + duration) % 7
  return DAY_OF_WEEK[nextDayOfWeek]

def get_military_time(hour, period):
  return hour if period == MORNING else hour + 12

def get_period(hour):
  day = hour % HOURS_IN_DAY
  return  MORNING if day < HOURS_IN_PERIOD else AFTERNOON

def get_days_later_description(daysLater):
  if daysLater == 0:
    return ""
  elif daysLater == 1:
    return " (next day)"
  else:
    return " (" + str(daysLater) + " days later)"

def get_twelve_hour_clock_time(hour):
  hourInTwelveHourClockTime = hour % HOURS_IN_PERIOD
  return HOURS_IN_PERIOD if hourInTwelveHourClockTime == 0 else hourInTwelveHourClockTime

def get_hour_to_display(hour):
  return str(hour)

def get_minute_to_display(minute):
  minuteAsString = str(minute)
  return "0" + minuteAsString if len(minuteAsString) == 1 else minuteAsString