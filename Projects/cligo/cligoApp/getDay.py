from datetime import date

class getDay():
    def get_day(self):
        dayofWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        today = str(date.today())
        day = [f.strip() for f in today.split('-')]
        
        oldDate = date(int(day[0]), int(day[1]), int(day[2])) # year, month, day
        
        return dayofWeek[date.weekday(oldDate)]