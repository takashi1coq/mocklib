from datetime import datetime, timedelta

def date_span(start_date, end_date):
    """start_date、end_dateの期間に含まれる日毎のdatetimeオブジェクトを返すジェネレータ
    """
    for n in range((end_date - start_date).days + 1):
        yield start_date + timedelta(n)
