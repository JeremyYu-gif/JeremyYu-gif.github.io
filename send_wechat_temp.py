# -*- coding: utf-8 -*-
import json
import urllib.request
import urllib.parse

WEBHOOK_URL = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=04883ea1-b729-4739-b563-6ea9e30f5e29"

stocks = [
    {"name": "Summit Therapeutics", "code": "SMMT", "recommendation": "HOLD", "rec_text": "持有", "reason": "短期回调不改长期逻辑"},
    {"name": "Biogen", "code": "BIIB", "recommendation": "ADD", "rec_text": "增仓", "reason": "Wells Fargo升级目标价$250"},
    {"name": "Ionis", "code": "IONS", "recommendation": "ADD", "rec_text": "增仓", "reason": "Zilganersen III期积极+新覆盖"},
    {"name": "Vor Biopharma", "code": "VOR", "recommendation": "HOLD", "rec_text": "持有", "reason": "无近期催化"},
    {"name": "Alnylam", "code": "ALNY", "recommendation": "HOLD", "rec_text": "持有", "reason": "底部整理等业绩催化"},
    {"name": "Vertex", "code": "VRTX", "recommendation": "HOLD", "rec_text": "持有", "reason": "均线收敛等方向"},
    {"name": "Acumen", "code": "ABOS", "recommendation": "HOLD", "rec_text": "持有", "reason": "小市值观望"},
    {"name": "AC Immune", "code": "ACIU", "recommendation": "HOLD", "rec_text": "持有", "reason": "Tau合作增强信心"},
    {"name": "药明生物", "code": "02269", "recommendation": "HOLD", "rec_text": "持有", "reason": "CXO龙头等板块修复"},
    {"name": "荣昌生物", "code": "688331", "recommendation": "ADD", "rec_text": "增仓", "reason": "维迪西妥单抗五项适应症"},
    {"name": "卓胜微", "code": "300782", "recommendation": "HOLD", "rec_text": "持有", "reason": "主力流入但业绩承压"},
    {"name": "有研新材", "code": "600206", "recommendation": "HOLD", "rec_text": "持有", "reason": "连续大涨高位震荡"}
]

report_url = "https://JeremyYu-gif.github.io/TOP-stock-daily-20260423.html"

# 构建消息
lines = ["### TOP股票跟踪日报 2026-04-23", ""]
lines.append("| 股票 | 操作建议 | 理由 |")
lines.append("|------|----------|------|")

for item in stocks:
    rec_icon = {"ADD": "🟩", "REDUCE": "🟥", "HOLD": "⬜"}.get(item.get("recommendation", "HOLD"), "⬜")
    name = item.get("name", "")
    code = item.get("code", "")
    rec_text = item.get("rec_text", "")
    reason = item.get("reason", "")
    lines.append(f"| {name}（{code}） | {rec_icon} {rec_text} | {reason} |")

lines.extend([
    "",
    f"> 📄 **完整HTML报告**",
    f"> {report_url}",
    "",
    "> 数据来源：StockAnalysis.com / Yahoo Finance / NeoData",
    "> 技术指标基于真实历史收盘价计算，仅供参考，不构成投资建议。"
])

message_text = "\n".join(lines)

message = {
    "msgtype": "markdown",
    "markdown": {
        "content": message_text
    }
}

data = json.dumps(message).encode("utf-8")
req = urllib.request.Request(
    WEBHOOK_URL,
    data=data,
    headers={"Content-Type": "application/json"}
)

try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        result = json.loads(resp.read())
        if result.get("errcode") == 0:
            print("企业微信推送成功！")
        else:
            print(f"企业微信推送失败：{result}")
except Exception as e:
    print(f"推送异常：{e}")