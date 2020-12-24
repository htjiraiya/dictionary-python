# from tructiepwidget import runtrigger as appRun

# from app import App
# import sys
import  os
from threading import Thread


def run1():
	os.system(f" python app.pyw ")



def run():
	os.system(f" python tructiepwidget.py ")



# link = r"C:\Users\htjir\OneDrive\Máy tính\nienluancs\tram\tudienpython\app.py"

if __name__ == "__main__":
	
	a = Thread(target=run1)
	a1 = Thread(target=run)

	a.start()

	a1.start()

