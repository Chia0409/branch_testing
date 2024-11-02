import csv
with open (file="./test.csv",  mode='r', encoding='utf-8') as f:
    csv_reader =csv.reader(f)
    for row in csv_reader:
        print(row)


# 開啟 CSV 檔案
with open('test.csv', mode='r', encoding='utf-8') as file:
    # 使用 csv.reader 讀取資料
    csv_reader = csv.reader(file)
    
    # 逐行讀取並顯示資料
    for row in csv_reader:
        print(row)

