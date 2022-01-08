s = input().split(' ')

start_i = int(ord(s[0]))
end_i = int(ord(s[-1]))
ls = []
for i in range(start_i,end_i+1):
    ls.append(chr(i))

ls = set(ls)
s = set(s)
new_s = list(ls-s)
new_s.sort()
print(new_s)