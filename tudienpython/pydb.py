import sqlite3


class Database():
	def __init__(self, name=None):
		if name is not  None :
			self.conn  = sqlite3.connect(name) 
			self.c = self.conn.cursor()	
			# return "thanh cong"

			

	def open(self, name): 
		self.conn  = sqlite3.connect(name) 
		self.c = conn.cursor()
		return "thanh cong"


	def execute(self,query, fetch_data = None):
		if fetch_data == "get data":
			self.c.execute(query)
			return self.c.fetchall()
		else:
			self.c.execute(query)
			self.conn.commit()
			return "thanh cong"

	def close(self):
		self.c.close()
		self.conn.close()	