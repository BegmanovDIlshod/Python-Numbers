from num2words import num2words

price1 = float(input('price1: '))
price2 = float(input('price2: '))
price3 = float(input('price3: '))

total = price1 + price2 + price3
yaxlit = round(total, 2)
eng = num2words(total, lang = 'en')
rus = num2words(total, lang = 'ru')

print(f'umumiy narx $ {total}, {eng}, {rus}')
print(f'yaxlitlangan narx $ {yaxlit}, {eng}, {rus}')