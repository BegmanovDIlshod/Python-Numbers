from num2words import num2words

pul = int(input('pul: '))
words = num2words(pul, lang = 'en')

pul_50 = pul // 50
pul = pul - pul_50 * 50

pul_10 = pul // 10
pul = pul - pul_10 * 10

pul_5 = pul // 5
pul = pul - pul_5 * 5

pul_1 = pul // 1
pul = pul - pul_1 * 1

total = pul_50 * 50 + pul_10 * 10 + pul_5 * 5 + pul_1 * 1

print(f' 50 $ kupyuradan: {pul_50} ta')
print(f' 10 $ kupyuradan: {pul_10} ta')
print(f' 5 $ kupyuradan: {pul_5} ta')
print(f' 1 $ kupyuradan: {pul_1} ta')
print(f'Umumiy summa $ {total}', num2words(total, lang = 'en'))