from num2words import num2words

servis_km = float(input('taxi km: '))
servis_bosh_tulov = 5.00

result = servis_bosh_tulov + servis_km * 0.8
yaxlit = round(result, 2)
eng = num2words(yaxlit, lang = 'en')
rus = num2words(yaxlit, lang = 'ru')

print(f'yetkazib berish narxi: {yaxlit}, {eng}, {rus}')
