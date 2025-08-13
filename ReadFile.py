import webbrowser
#Bai tap doc file tu he thong
a="" #Khai bao bien 
print("Nhap ten file ban muon mo: ") #In man hinh yeu cau nhap input
file = open(input(a)) #doc input tu ban phim va gan vao file
# print(file.read()) #in man hinh noi dung file
webbrowser.open(file.read())
file.close() #dong file;

