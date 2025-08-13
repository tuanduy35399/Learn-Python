import csv

# with open("csv_f.txt", "r") as f:
#     csv_f= csv.reader(f)
#     for row in csv_f:
#         tenHP, maHP, TC= row
#         print("Tên học phần {}\nMã học phần {}\nSố tính chỉ {}\n.................".format(tenHP, maHP, TC))

#thêm học phần

danh_sach = [
    {
    "name": "Toan roi rac",
    "maHP": "CT101H",
    "soTC": "3"
    },
    {
    "name": "Vi tich phan",
    "maHP": "CT111H",
    "soTC": "4"
    },
    {
    "name": "Dai so tuyen tinh",
    "maHP": "CT131H",
    "soTC": "3"
    }
    ]
keys=["name", "maHP", "soTC"]
with open("csv_f.txt", "w") as file:
    csv_f= csv.DictWriter(file, fieldnames=keys)
    csv_f.writeheader()
    csv_f.writerows(danh_sach)
with open("csv_f.txt", "r") as file:
    csv_f=csv.DictReader(file)
    for row in csv_f:
        print("Tên học phần: {}\nMã học phần: {}\nSố tính chỉ: {}\n.................".format(row["name"], row["maHP"], row["soTC"]))