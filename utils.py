import datetime
def get_date_month():
    now = datetime.datetime.now()
    year_month = now.strftime("%Y-%m")
    return year_month