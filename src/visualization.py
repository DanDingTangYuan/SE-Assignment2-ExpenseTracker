import pandas as pd
import matplotlib.pyplot as plt

# 設定中文顯示（若類別為英文可省略）
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

def generate_pie_chart():
    try:
        # 1. 讀取成員 A 的資料 [cite: 8, 9]
        df = pd.read_csv('expenses.csv')
        
        # 2. 依 Category 加總 Amount [cite: 12]
        category_totals = df.groupby('Category')['Amount'].sum()
        
        # 3. 建立畫布
        plt.figure(figsize=(10, 7))
        
        # 繪製圓餅圖：
        # labels=None 隱藏圖上標籤
        # autopct 顯示百分比
        wedges, texts, autotexts = plt.pie(
            category_totals, 
            labels=None, 
            autopct='%1.1f%%', 
            startangle=140,
            textprops={'color':"w", 'weight':'bold'} # 百分比設為白色粗體
        )
        
        # 4. 加入獨立圖例方塊 (Legend)
        # loc="upper left" 設定在左上角
        # bbox_to_anchor 調整位置，確保不會擋到圖
        plt.legend(
            wedges, 
            category_totals.index,
            title="消費類別",
            loc="center left",
            bbox_to_anchor=(1, 0, 0.5, 1)
        )
        
        plt.title('費用類別佔比分析') 
        plt.tight_layout() # 自動調整佈局防止遮擋
        
        # 儲存截圖以便放入 README 
        plt.savefig('sample_pie_chart.png')
        print("圖表已生成並儲存為 sample_pie_chart.png")
        plt.show()
        
    except FileNotFoundError:
        print("錯誤：找不到 expenses.csv，請先執行輸入模組。") [cite: 13]

if __name__ == "__main__":
    generate_pie_chart()