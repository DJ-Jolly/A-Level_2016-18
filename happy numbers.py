def Happy_number(num):
    unhappy_list = set()
    while num != 1:
	num = sum(int(i)**2 for i in str(n))
	if num in unhappy_list:
	    return false
	unhappy_list.add(num)
    return true

num = int(input(“What number would you like to test:”))
