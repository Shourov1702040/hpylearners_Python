def fact(n):  
    return 1 if (n==1 or n==0) else n * fact(n - 1);  

def check_special(num_st):
	sum_t = 0
	for i in num_st:
		sum_t += fact(int(i))
	if int(num_st)==sum_t:
		return True
	else:
		return False
lst = input().split(', ')
special = []
non_special = []
for i in lst:
	if check_special(i):
		special.append(i)
	else:
		non_special.append(i)
special = tuple(special)
non_special =tuple(non_special)

this_dict = {'Special': special, 'Non-Special':non_special}
print(this_dict)
