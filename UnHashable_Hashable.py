a= id(5)
print(a)
#id() trả về địa chỉ nơi đang lưu giá trị đó trên bộ nhớ
# Đối với int thì địa chỉ là hằng số, còn string, list địa chỉ là 1 biến số thay đổi liên tục

# Unhashable: Là kiểu object có thể thay đổi nội dung sau khi tạo (mutable).
# Nếu cho phép hash, hash value sẽ thay đổi khi nội dung thay đổi, 
# gây lỗi logic khi dùng làm key trong dict hoặc phần tử set. 
# Python chặn điều này bằng cách không cho hash ngay từ đầu.
#Ví dụ: list, dict, set

# Hashable: Là kiểu object có giá trị băm cố định trong suốt vòng đời. 
# Thường là immutable, nên mọi “thay đổi” thực chất tạo ra object mới ở địa chỉ khác.
#Ví dụ: int, str, tuple, frozenset