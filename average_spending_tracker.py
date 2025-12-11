
from num2words import num2words

du = float(input('du: '))
se = float(input('se: '))
chor = float(input('chor: '))
pay = float(input('pay: '))
ju = float(input('ju: '))
shan = float(input('shan: '))
yak = float(input('yak: '))


total = (du + se + chor + pay + ju + shan + yak) / 7
yaxlit = round(total,2)
print(f' O\'rtacha xarajat: {yaxlit}', num2words(yaxlit, lang = 'en'), num2words(yaxlit, lang = 'ru'))