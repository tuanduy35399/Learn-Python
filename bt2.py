# Nhập vào số n, hãy mũ 2 rồi chia cho 3, sau đó in kết quả ra màn hình
# import math
# n= int(input())
# print(int(math.pow(n,2)//3))

# Nhập vào một số nguyên a, nếu a chia hết cho 2 thì in ra True, ngược lại in ra False

# a= int(input())
# if a%2==0 :
#     print(True)
# else:
#     print(False)

# Nhập vào số nguyên a, nếu a là số chia hết cho 5
# nhưng KHÔNG nằm trong khoảng từ 20 - 70 thì in ra True, ngược lại in ra False
# a = int(input())
# if a%5==0 and a not in range(20,70+1):
#     print(True)
# else:
#     print(False)

# Find max
# def max (a: int, b: int):
#     return a if a>b else b

# Nhập vào lương tháng này nhận được, ta phải đưa cho 
# vợ 90% số tiền lương đó. Hãy in ra lương ta giữ lại

# a=int(input())
# print(int(a-(a*0.9)))
#Print a star triangle
# for i in range(1,10+1):
#     for j in range(1,i+1):
#         print("* ", end="")
#     print()

# Write a Python program that converts a number of seconds
# into hours, minutes, seconds, e.g.: 13806 = 03h50m06s.

# n= int(input())
# h= n//3600
# m=(n%3600) //60
# s=(n%3600) %60
# print("{:02d}:{:02d}:{:02d}".format(h,s,m))

# Viết chương trình in danh sách sinh viên sau ra màn hình

# STT	Ma SVien	Ho va ten
# 1	    B1606869	Thai Bao
# 2	    B1800169	Le Tuong Dung
# 3	    B1805707	Vuong Tam Nhu

print("{:<5} {:<10} {:<20}".format("STT", "Ma SVien", "Ho va ten"))
print("{:<5} {:<10} {:<20}".format("1", "B1606869", "Thai Bao"))
print("{:<5} {:<10} {:<20}".format("2", "B1800169", "Le Tuong Dung"))
print("{:<5} {:<10} {:<20}".format("2", "B1805707", "Vuong Tam Nhu"))