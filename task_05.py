import datetime
def date_in_future(integer=''):
    if integer=='' or type(integer)!=int:
        now_datetime=datetime.datetime.now()
        return now_datetime.strftime('%d-%m-%Y %H:%M:%S')
    else:
        now_datatime=datetime.datetime.now()
        ft_datetime = now_datatime+datetime.timedelta(days=integer)
        return ft_datetime.strftime('%d-%m-%Y %H:%M:%S')

date_in_future()  #--> текущая дата
date_in_future(2)  #--> текущая дата + 2 дня