from datetime import datetime,date
class_12_first_exam_date="2026-3-27 8:00 "
cfex=datetime.strptime(class_12_first_exam_date, "%Y-%m-%d%I:%M ").date()
today=date.today()
month_passed=(today.year-cfex.year)*12+(today.month-cfex.month)
if today.day<cfex.day:
    month_passed-=1
print(f' The time i have commite fully my self desire and consciouess to take my body and handle my own problem :{month_passed} month')