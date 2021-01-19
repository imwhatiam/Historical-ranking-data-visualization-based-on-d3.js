import csv
import datetime

date_list = [
    '2012.03.31',
    '2012.06.30',
    '2012.09.30',
    '2012.12.31',
    '2013.03.30',
    '2013.06.30',
    '2013.09.30',
    '2013.12.31',
    '2014.03.31',
    '2014.06.30',
    '2014.09.30',
    '2014.12.31',
    '2015.03.31',
    '2015.06.30',
    '2015.09.30',
    '2015.12.31',
    '2016.03.31',
    '2016.06.30',
    '2016.09.30',
    '2016.12.31',
    '2017.03.31',
    '2017.06.30',
    '2017.09.30',
    '2017.12.31',
    '2018.03.31',
    '2018.06.30',
    '2018.09.30',
    '2018.12.31',
    '2019.03.31',
    '2019.06.30',
    '2019.09.30',
    '2019.12.31',
    '2020.03.31',
    '2020.06.30',
    '2020.09.30',
    '2020.12.31',
    '2021.01.01'
]

mdd_date_list = []
with open('data.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        mdd_date_list.append(row)


data = []
with open('result.csv', 'w', encoding='utf-8', newline='') as f:

    writer = csv.writer(f)
    writer.writerow(['name', 'type', 'value', 'date'])

    for date_str in date_list:

        date_limit = datetime.datetime.strptime(date_str, "%Y.%m.%d")

        mdd_count_dict = {}

        for mdd_date_str in mdd_date_list:

            mdd = mdd_date_str[0]
            date = datetime.datetime.strptime(mdd_date_str[1], "%Y.%m.%d")

            if date > date_limit:
                break

            if mdd not in mdd_count_dict:
                mdd_count_dict[mdd] = 1
            else:
                mdd_count_dict[mdd] += 1

        for mdd, count in mdd_count_dict.items():
            data.append([mdd, mdd, str(count), date_str])

    writer.writerows(data)
