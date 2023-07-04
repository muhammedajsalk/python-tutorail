from datetime import datetime
date_string="21 June, 2018"
date_object= datetime.strptime(date_string,"%d %B, %Y")
print(date_string)
print(date_object)
#21 June, 2018
#2018-06-21 00:00:00