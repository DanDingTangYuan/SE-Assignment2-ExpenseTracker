import expense_input  # 成員 A 的模組
import visualization  # 成員 B (您) 的模組

def main():
    while True:
        print("\n===== 費用追蹤工具主選單 =====")
        print("1. 錄入費用 (Member A)")
        print("2. 生成圓餅圖 (Member B)")
        print("3. 退出")
        
        choice = input("請選擇功能 (1/2/3): ")
        
        if choice == '1':
            expense_input.initialize_file()
            while True:
                expense_input.add_expense() 
                cont = input("是否繼續輸入? (y/n): ")
                if cont.lower() != 'y':
                    break
            # 確保 A 的檔案中有此函式
        elif choice == '2':
            visualization.generate_pie_chart() # 執行您的視覺化功能
        elif choice == '3':
            break
        else:
            print("無效選擇，請重試。")

if __name__ == "__main__":
    main()