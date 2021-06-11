a = int(input())
b = int(input())
print("{}\n{}\n{}\n{}".format(a*(b%10),a*int((b%100)/10),a*int(b/100),a*b))