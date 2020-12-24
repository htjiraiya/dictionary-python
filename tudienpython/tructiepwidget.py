from PyQt5 import QtCore, QtGui, QtWidgets
from tructiepwidget_ui import Ui_Form
import sys
import  pyperclip
from pynput import keyboard
import subprocess
from pynput import keyboard
from threading import  Thread
from tructiepwidget import Ui_Form
from google_trans_new import google_translator  
from pydb import Database
from datetime import datetime
from PyQt5.QtGui import  QIcon


string = ""
db = Database("./database/data_word.db")

def function_2(): 
	global string


	if string != pyperclip.paste():
		string = pyperclip.paste()
	# app = QtWidgets.QApplication(sys.argv)
	# ui = AppWidget()
	# ui.ui.textEdit.setPlainText(string)
	# ui.show()
	print(string)
	# sys.exit()
	# while True:
	# Thread(target=trigger_ctrl_c).start()
	# global string
	app = QtWidgets.QApplication(sys.argv)
	ui = AppWidget()
	ui.ui.textEdit.setPlainText(pyperclip.paste().lower())
	# 
	ui.dich()

		
	sys.exit(app.exec_())



def trigger_ctrl_c():
    with keyboard.GlobalHotKeys({
    '<ctrl>+c': function_2}) as h:
        h.join()


class AppWidget(QtWidgets.QWidget):
	def __init__(self):
		super().__init__()
		self.ui = Ui_Form()
		self.ui.setupUi(self)
		self.show()
		self.db = Database("./database/data_word.db")
		self.translator =  google_translator()  
		self.setWindowIcon(QIcon('./anh/icon/icon.png')) 
	def dich(self):	
		
		text = self.ui.textEdit.toPlainText()
		query = f"SELECT * FROM word WHERE e_word like '{text}'"
		try:
			get_return = self.db.execute(query,"get data")
			if len(get_return)  < 1:
				self.ui.textEdit.setPlainText("")
				# self.ui.textEdit.setPlainText("từ này không tồn tại")
				text_out_put = self.translator.translate(text,lang_tgt='vi')
				self.ui.textEdit.setPlainText(text_out_put)
				# text_out_put = ""
			else:
				print(get_return)
				word = get_return[0][0]
				tu_loai = get_return[0][1]
				phat_am = get_return[0][2]
				mieu_ta = get_return[0][3]
				nghia = get_return[0][4]
				self.show_return =f"Từ: {word}\nTừ loại: {tu_loai}\nPhát âm: {phat_am}\nMiêu tả: {mieu_ta}\nNghĩa: {nghia}" 
				self.ui.textEdit.setPlainText(f"Từ: {word}\nTừ loại: {tu_loai}\nPhát âm: {phat_am}\nMiêu tả: {mieu_ta}\nNghĩa: {nghia}")
				# /// log
				with open(f"./database/log_word.txt",'a', encoding="utf-8") as f:
					content = str(datetime.now()).split(" ")[0] + f"\nTừ: {word}\nTừ loại: {tu_loai}\nPhát âm: {phat_am}\nMiêu tả: {mieu_ta}\nNghĩa: {nghia}"
					content += "\n-----------------------------\n"
					f.write(f'{content}')
		except :

			# if len(get_return)  < 1:
			self.ui.textEdit.setPlainText("")
			try:
				text_out_put = self.translator.translate(text,lang_tgt='vi')
				self.ui.textEdit.setPlainText(text_out_put)
			except:
				self.ui.textEdit.setPlainText("có một số lỗi có thể về kết nối")

	def log(self):
		with open(f"./database/log_word.txt",'a') as f:
			content = str(datetime.now()).split(" ")[0] + f"\nTừ: {word}\nTừ loại: {tu_loai}\nPhát âm: {phat_am}\nMiêu tả: {mieu_ta}\nNghĩa: {nghia}"
			content += "-----------------------------\n"
			f.write(f'{content}')
# if __name__ == "__main__":
def runtrigger():
	while  True:
		trigger_ctrl_c()




runtrigger()
# print("hi")
#ahihi