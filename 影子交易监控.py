import requests
import time
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

SLUG = os.getenv("SLUG")
CONDITION_ID = os.getenv("CONDITION_ID")

def get_market_tokens():
    """获取该市场下 Yes 和 No 的所有 Token 信息"""
    url = f"https://clob.polymarket.com/markets/{CONDITION_ID}"
    res = requests.get(url).json()
    return {t['outcome']: t['token_id'] for t in res['tokens']}

def get_market_detail(token_id):
    """获取指定 Token 的实时买卖价和深度"""
    # side=BUY 获取买单详情，side=SELL 获取卖单详情
    buy_url = f"https://clob.polymarket.com/price?token_id={token_id}&side=BUY"
    sell_url = f"https://clob.polymarket.com/price?token_id={token_id}&side=SELL"
    
    try:
        buy_price = float(requests.get(buy_url).json().get('price', 0))
        sell_price = float(requests.get(sell_url).json().get('price', 0))
        return buy_price, sell_price
    except:
        return 0.0, 0.0

def monitor():
    print(f"🚀 开始深度监控市场: {SLUG}")
    tokens = get_market_tokens()
    yes_id = tokens['Yes']
    no_id = tokens['No']
    
    last_yes_price = 0
    
    print(f"{'时间':<20} | {'Yes买价':<10} | {'Yes卖价':<10} | {'价差(Spread)':<10} | {'合规检查'}")
    print("-" * 75)

    while True:
        now = datetime.now().strftime("%H:%M:%S")
        y_buy, y_sell = get_market_detail(yes_id)
        n_buy, n_sell = get_market_detail(no_id)
        
        # 1. 计算价差 (Spread) - 价差越大，用户交易成本越高，越“难用”
        spread = abs(y_sell - y_buy) if y_sell > 0 else 0
        
        # 2. 检查价格偏差 (Sum Check) - 理论上 Yes买价 + No买价 应该接近 $1
        sum_price = y_buy + n_buy
        status = "✅ 正常" if 0.98 <= sum_price <= 1.02 else f"⚠️ 偏差 ({sum_price:.3f})"
        
        # 3. 剧烈波动报警
        if last_yes_price != 0 and abs(y_buy - last_yes_price) > 0.02:
            print(f"\n🚨 [波动报警] Yes价格从 {last_yes_price} 急剧跳动至 {y_buy}! \n")
        
        print(f"{now:<20} | {y_buy:<10.3f} | {y_sell:<10.3f} | {spread:<12.3f} | {status}")
        
        last_yes_price = y_buy
        time.sleep(10) # 每10秒监控一次

if __name__ == "__main__":
    monitor()