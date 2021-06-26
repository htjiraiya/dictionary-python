# doc file
# neu @ thi dinh nghia no la tu moi
# them dong vao tu dinh nghia 


from pydb import Database


path = r"./database/data_word.db"
database = Database(path)
path = 'tu.txt'
file = open(path,'r',encoding='utf-8')
file = file.readlines()
list_tu = []
word = []
for line in file:	
	if '@' in line:
		# tu moi
		list_tu.append(word)
		word = []
		word.append(line)
		continue
	word.append(line)
# print(list_tu)
del list_tu[0]
# tap 2 
# thag 1
i  = 0
# 22016
# 25280
for word in list_tu:
	i += 1
	if i > 25280:
	# 	break
	# thang 1 
	# chia thanh tu va am
	# tu, am = word[0].split(" /")
		try:

			tu = word[0].split(" /")[0]
			tu = tu.replace('"',"")
		except :
			tu = "none"

		try:

			am = word[0].split(" /")[1]
			am = am.replace("/", "")
		except :
			am = ""
		try:
			tuloai = word[1]
			tuloai = tuloai.replace('"',"")
		except:

			tuloai = ""
		
		try:
			nghia = word[2]
			nghia = nghia.replace('"',"")
		except:

			nghia = ""
			
		mieuta = ""
		try :
			mieuta = word[3]
			mieuta = mieuta.replace('"',"")
		except :
			mieuta = ""

		tu = tu[1:].strip()
		tuloai = tuloai[1:].strip()
		nghia =nghia[1:].strip()
		mieuta = mieuta[1:].strip()
		am = am.strip()
		# print(f'tu: {tu} \nam: {am} \ntuloai: {tuloai} \nnghia: {nghia} \nmieuta: {mieuta}')
		try:
			query = f'INSERT INTO word (e_word, e_type, e_pronouce, e_des, e_mean) VALUES ("{tu}", "{tuloai}","{am}", "{mieuta}","{nghia}")'
			database.execute(query)
		# time.sleep(0.5)
		except :
			query = f"INSERT INTO word (e_word, e_type, e_pronouce, e_des, e_mean) VALUES ('{tu}', '{tuloai}','{am}', '{mieuta}','{nghia}')"
			database.execute(query)

	# for element in word:
	# 	print(element)
	# 	break
	# 	# tu, am = element[0].split(" /")
	# 	# a = element[0].split(" /")
	# 	# print(a)
	# 	# break
	# 	# tuloai = element[1]
	# 	# nghia = element[2]
	# 	# mieuta = ""
	# 	# try:
	# 	# 	mieu = element[3]
	# 	# except :
	# 	# 	pass
