deg = input('請輸入攝氏溫度(-999~999) ：') #deg = degree (溫度)
deg = float(deg)
fah = deg * ( 9 / 5 ) + 32 #fah=fahrenheit(華氏溫度) deg*(9/5)+32
if deg >= -99999999999:
    print('華氏溫度 = ', fah, '度')