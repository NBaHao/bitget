import string
import requests
import telegram
import time
import bitget.mix.market_api as market
import bitget.mix.account_api as accounts
import bitget.mix.position_api as position
import bitget.mix.order_api as order
import bitget.mix.plan_api as plan
import bitget.mix.trace_api as trace
import json

token = "5749467164:AAGTEXdsOO1IousGFqt6RSNYI1Zi8rJ5-VA"
bot = telegram.Bot(token = token)

chat_id = '@onganhcubu'

#chat_id = "-1001488547835"

if __name__ == '__main__':
    api_key = 'bg_39285920cf0180229961310623e770dc'
    secret_key = "ecd40860bfba42d7fe17eaf7ec6c7d0597c111d77d87ad103083e58573e41f3a"
    passphrase = "0933952251Aa"
    symbol = 'SBTCSUSDT_SUMCBL'
    pageSize = 0
    
    startTime = '1662201378986'
    endTime = '1762219658744'

    orderApi = order.OrderApi(api_key, secret_key, passphrase, use_server_time=True, first=True)
    positionApi = position.PositionApi(api_key, secret_key, passphrase, use_server_time=True, first=True)
    accountApi = accounts.AccountApi(api_key, secret_key, passphrase, use_server_time=False, first=False)
    TraceApi = trace.TraceApi(api_key, secret_key, passphrase, use_server_time=False, first=False)

    result = orderApi.historyProductType('SUMCBL', startTime, endTime, 500)
    #print(result)
    cnt = 0
    for res in result['data']['orderList']:
        cnt=cnt+1
    while True:
        result = orderApi.historyProductType('SUMCBL', startTime, endTime, 500)
        tcnt = len(result['data']['orderList'])
        if (cnt < tcnt):
            for res in result['data']['orderList']:
                if (res['orderType'] == "limit"):
                    bot.sendMessage(chat_id = chat_id , text=res['symbol']+"\n" + res['side'] + "\nleverage: " + res['leverage'] + "\nprice: "+str(res['price']))
                else:
                    bot.sendMessage(chat_id = chat_id , text=res['symbol']+"\n" + res['side'] + "\nleverage: " + res['leverage'] + "\nprice: "+str(res['priceAvg']) + "\nvol: " + str(res['size']))
                break
            cnt=tcnt
# hahahahahahahah