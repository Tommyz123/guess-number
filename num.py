import random


r = random.randint(1,10)

while True:
	num = input('请输入你要猜的数字： ')
	num = int(num)
	if r != num:
		print('你猜错了 ')

		if num > r:
			print('你的数字大了')

		elif num < r:
			print('你的数字小了')

	else:
		print('你猜对了。')
		break


