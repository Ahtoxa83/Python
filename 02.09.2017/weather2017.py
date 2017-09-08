lines = [] # Создаём сводный список для даты, температуры, осадков
days_in_all_period = {} # Словарь для средней температуры за весь период
number_of_measuring_in_days = {} # Словарь для количества измерений температуры за весь период
average_temp = [] # Список для средней температуры
days_withoutrain = {} # Дней без дождя
days = 0
count = 0
all_temp = 0

with open ("weather2017.csv", "r", encoding = "utf-8") as f:

	for line in f:
		line = line[:-1].replace('";"', '" ; "') 
		line = line.replace ('"', '') # Удаляем лишние знаки из строки
		line = line.split(' ; ') # Разбиваем строку
		date = line[0][:10] 
		temp = line[1]
		prec = line[23]
		lines.append([date, temp, prec])

	number_of_measuring_in_days[days] = 0
	
	for day in lines:
		metering = day[0]
		days = day[0]
		no_rain = day[0]

		if day[2] == "Осадков нет":
			days_withoutrain[no_rain] = day[2]

		try:
			number_of_measuring_in_days[days] += 1
			days_in_all_period[metering] += float(day[1])

		except KeyError:
			number_of_measuring_in_days[days] = 1
			days_in_all_period[metering] = float(day[1])

	for days in days_in_all_period:
		count += 1
		for i in number_of_measuring_in_days:
			if days == i:
				temp = days_in_all_period[days] / number_of_measuring_in_days[i]
				all_temp += temp
				average_temp.append ([temp, days])



raining_days = (len(days_in_all_period) - len(days_withoutrain))
avg_temp = round((all_temp/len(days_in_all_period)), 2)
minimal_t = min(average_temp)
maximum_t = max(average_temp)

result = 'Средняя температура за всё лето, составила:{t}. Всего дождливых дней:{r}. \
Самый тёплый день был {max}, а холодный {min}.'.format(t=avg_temp, r=raining_days, max=maximum_t[1], min=minimal_t[1])

print (result)