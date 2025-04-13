import requests
from datetime import datetime

def generate_report():
    # 获取Base链新币数据
    url = "url = "https://api.dexscreener.com/latest/dex/tokens/solana"
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    data = response.json()

    # 生成HTML报告
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Meme币扫描 {datetime.now().strftime('%Y-%m-%d %H:%M')}</title>
        <style>
            body {{ font-family: Arial; margin: 20px; }}
            table {{ border-collapse: collapse; width: 100%; }}
            th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
            tr:nth-child(even) {{ background-color: #f2f2f2; }}
        </style>
    </head>
    <body>
        <h1>🔥 最新Meme币监测</h1>
        <table>
            <tr>
                <th>币种</th>
                <th>价格(USD)</th>
                <th>流动性</th>
                <th>交易对</th>
                <th>年龄(小时)</th>
            </tr>
            {"".join(
                f"""
                <tr>
                    <td>{pair['baseToken']['symbol']}</td>
                    <td>{float(pair['priceUsd']):.6f}</td>
                    <td>${float(pair['liquidity']['usd']):,.0f}</td>
                    <td>{pair['dexId']}</td>
                    <td>{round((datetime.now().timestamp() - pair['pairCreatedAt']/1000)/3600, 1)}</td>
                </tr>
                """
                for pair in data['pairs'][:10]  # 显示前10个
            )}
        </table>
    </body>
    </html>
    """
    
    with open('report.html', 'w') as f:
        f.write(html)
    print("报告已生成")

if __name__ == '__main__':
    generate_report()
