# Cau truc du lieu Tuple linh hoạt, khá giống list
# Function có thể trả về nhiều giá trị được bao lại thành 1 tuple
# Generator expression 
# Khác với List comprehension ở chỗ List dùng [] và lưu dữ liệu ngay gây tốn bộ nhớ
# còn generator expression thì sinh dữ liệu chỉ 1 lần duyệt và sẽ biến mất 
# nên cần 1 biến kiểu tuple hoặc list để lưu.
# gener chỉ dùng được 1 lần nên để tạo ra 2 tuple hoặc list thì cần 2 gener
# tuple sẽ không thể thay đổi được trừ khi khởi tạo lại (ko có append, insert, extend giống list)

# a= tuple(i for i in range(1,11))
# print(type(a))
# print(a)

# def sum(a,b):
#     return a,b,a+b

# s=sum(2,7)
# print(s)
# print(type(s))
# a,b,c= s
# print("{} + {} = {}".format(a,b,c))
# toán tử trong tuple
# Giống chuỗi khi có thể nối thông qua +, tăng số lượng lên qua *
#Tuple
tup=(1,2,3)
tup+=(4,5,6)
print(tup)
tup*=3
print(tup)
#String
a='Hello'
a+=' Tuan Duy'
print(a)
a*=3
print(a)

