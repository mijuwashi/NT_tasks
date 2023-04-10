import json

with open('C:\Users\Lenovo\Downloads\tests.json', 'r') as f1, open('C:\Users\Lenovo\Downloads\values.json', 'r') as f2:
    tests_data = json.load(f1)
    values_data = json.load(f2)

for test in tests_data:
    for value in values_data:
        if value['id'] == test['id']:
            test['value'] = value['value']
    for val in test['values']:
        if val['id'] == value['id']:
            val['value'] = value['value']

with open('report.json', 'w') as f3:
    json.dump(tests_data, f3)
