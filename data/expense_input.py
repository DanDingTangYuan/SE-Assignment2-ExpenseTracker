import csv
import os
from datetime import datetime

# 檔案名稱
FILE_NAME = 'expenses.csv'

def initialize_file():
    """初始化 CSV 檔案，如果不存在則建立標題列"""
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Date', 'Amount', 'Category', 'Notes'])

def add_expense():
    """新增一筆消費紀錄"""
    print("--- 新增消費紀錄 ---")

    # 取得日期
    date_str = input("請輸入日期 (YYYY-MM-DD，直接按 Enter 為今天): ")
    if not date_str:
        date_str = datetime.now().strftime("%Y-%m-%d")

    # 取得金額
    while True:
        try:
            amount = float(input("請輸入金額: "))
            break
        except ValueError:
            print("輸入錯誤，請輸入有效的數字。")

    # 取得類別
    print("類別範例: 食物, 交通, 娛樂, 房租, 其他")
    category = input("請輸入類別: ")

    # 取得備註
    notes = input("備註 (可選): ")

    # 寫入檔案
    with open(FILE_NAME, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([date_str, amount, category, notes])

    print("已成功儲存！")

if __name__ == "__main__":
    initialize_file()
    while True:
        add_expense()
        cont = input("是否繼續輸入? (y/n): ")
        if cont.lower() != 'y':
            break