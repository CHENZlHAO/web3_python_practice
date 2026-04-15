import pandas as pd
import requests
import json

# 配置（在此处填入你的信息）
POLYGON_RPC_URL = "https://polygon-mainnet.g.alchemy.com/v2/ezzUB6wzRH1vWlvdIC948"
GRAPH_URL = "https://api.thegraph.com/subgraphs/name/polymarket/clob-schema-mainnet" # Polymarket 数据节点
def get_polymarket_positions(wallet_address):
    # GraphQL 查询语句：获取该地址持有的仓位
    query = """
    {
      userPositions(where: {user: "%s", advocacy_gt: 0}) {
        id
        condition {
          description
          question
        }
        advocacy
        netAmount
      }
    }
    """ % wallet_address.lower()

    try:
        response = requests.post(GRAPH_URL, json={'query': query})
        data = response.json()
        
        positions = data['data']['userPositions']
        if not positions:
            return pd.DataFrame()

        # 数据清洗与结构化
        cleaned_data = []
        for pos in positions:
            cleaned_data.append({
                "Question": pos['condition']['question'],
                "Amount": pos['netAmount'],
                "Position_ID": pos['id']
            })
        
        return pd.DataFrame(cleaned_data)
    
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None
if __name__ == "__main__":
    user_address = input("请输入要查询的 Polygon 钱包地址: ")
    
    print(f"正在查询 {user_address} 的 Polymarket 持仓...")
    df = get_polymarket_positions(user_address)

    if df is not None and not df.empty:
        print("\n--- 持仓清单 ---")
        print(df)
        # 导出为 CSV 方便查看
        df.to_csv("my_positions.csv", index=False)
        print("\n数据已保存至 my_positions.csv")
    else:
        print("未发现持仓或地址输入错误。")