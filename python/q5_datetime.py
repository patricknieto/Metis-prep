# Hint:  use Google to find python function

import datetime as dt
from datetime import datetime

def days_betweena(d1, d2):
	d1 = datetime.strptime(d1, "%m-%d-%Y")
	d2 = datetime.strptime(d2, "%m-%d-%Y")
	return (d1-d2).days

def days_betweenb(d1, d2):
	d1 = datetime.strptime(d1, "%m%d%Y")
	d2 = datetime.strptime(d2, "%m%d%Y")
	return (d1-d2).days

def days_betweenc(d1, d2):
	d1 = datetime.strptime(d1, "%d-%b-%Y")
	d2 = datetime.strptime(d2, "%d-%b-%Y")
	return (d1-d2).days
	

####a) 
date_starta = '01-02-2013'  
date_stopa = '07-28-2015'   

####b)  
date_startb = '12312013'  
date_stopb = '05282015'  

####c)  
date_startc = '15-Jan-1994'  
date_stopc = '14-Jul-2015'


days_betweena(date_stopa, date_starta)
937

days_betweenb(date_stopb, date_startb)
513

days_betweenc(date_stopc, date_startc)
7850




