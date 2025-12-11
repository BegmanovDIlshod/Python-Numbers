from num2words import num2words

oy_oxiridagi_kursatgich = float(input('oy oxiridagi kursatgich: '))
oy_boshidagi_kursatgich = float(input('oy boshidagi kursatgich: '))

narx = 0.45 

result = (oy_oxiridagi_kursatgich - oy_boshidagi_kursatgich) * narx
yaxlit = round(result, 2)
eng = num2words(yaxlit, lang = 'en')
rus = num2words(yaxlit, lang = 'ru')

print(f' to\'lov: {yaxlit} ({eng}, {rus}')
