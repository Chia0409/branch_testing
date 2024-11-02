import pandas as pd
import numpy as np

#開啟excel
excel = pd.read_excel(".\新增 Microsoft Excel 工作表.xlsx")
# print(excel)


column_list =[]
index_list =[]
for column in excel:
    column_list.append(column)
    for index in excel:
        index_list.append(index)
        print(column,index)
        
    
    # print(column)

# for index, row in excel.iterrows():
#     print(f"\n學號: {row['學號']}")
#     for subject in column_list[1:]:  # 略過 "學號" 欄位，從第2欄開始
#         print(f"{subject}: {row[subject]}")
   
   
#寫入excel
