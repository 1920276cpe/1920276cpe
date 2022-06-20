import csv

fieldnames = ['name','area','country_code2','country_code3']

rows = [
    {'name':'Albania', 'area': 28748, 'country_code2': 'AL', 'country_code3': 'ALB'},
    {'name': 'Algeria', 'area': 23142, 'country_code2': 'DZ', 'country_code3': 'DZE'},
    {'name': 'American Samoa', 'area': 199, 'country_code2': 'AS', 'country_code3': 'ASM'}
    ]

with open('static/ch11_12/countries.csv','w',encoding="utf8", newline='') as f:
    writer = csv.DictWriter(f, fieldnames = fieldnames)
    writer.writeheader()
    writer.writerows(rows)
