import datetime
from datetime import time, date

format = '%Y-%m-%d %H:%M'

timing = [
    "08:00",
    "10:00",
    "12:00",
    "14:00",
    "16:00"
]

TIME_SLOTS = [

]


for t in timing:

    try:
        res = datetime.datetime.strptime("{0} {1}".format(date.today(), t), format)
    except TypeError:
        res = datetime.datetime(*(time.strptime("{0} {1}".format(date.today(), t), format)[0:6]))

    TIME_SLOTS.append(res)


TUP_SLOTS = tuple(TIME_SLOTS)
