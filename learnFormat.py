a,b,c= 2,3,2+3
print("{} + {} = {}".format(a,b,c))
print("{i} + {j} = {h}".format(i=a,j=b,h=c))
print("{i:02d} + {j:02d} = {h:02d}".format(i=a,j=b,h=c))
print("{:>2d} + {:>2d} = {:>2d}".format(a,b,c))
print("{:0>2d} + {:$>2d} = {:#>2d}".format(a,b,c))
#Sự khác nhau giữa :02d và :0>2d linh hoạt hơn khi có thể thay số 0 trong :0>2d bằng ký tự khác