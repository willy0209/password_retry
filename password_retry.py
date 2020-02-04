x = 3
password = 'a123456'
while x > 0:
	x = x-1
	psw = input('請輸入密碼: ')
	if psw == password:
		print('登入成功')
		break
	else:
		if x > 0:
			print('密碼錯誤','還有', x, '次機會')
		else:
			print('你沒機會了')