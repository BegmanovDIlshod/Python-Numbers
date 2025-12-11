

from num2words import num2words

taxi_km = float(input('taxi km: '))
taxi_bosh_tulov = 3.0

result = taxi_bosh_tulov + taxi_km * 1.2
eng = num2words(result, lang = 'en')
rus = num2words(result, lang = 'ru')

print(f'taxi narxi: {result}, {eng}, {rus}')

