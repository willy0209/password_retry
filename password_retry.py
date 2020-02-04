x = 3
password = 'a123456'
while True:
	psw = input('請輸入密碼: ')
	if psw == password:
		print('登入成功')
		break
	else:
		x = x-1
		print('還有', x, '次機會')
		if x == 0:
			break