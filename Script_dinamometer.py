import csv

'''

Adicionar este header em todos os seus csvs e rodar o scripts - 'Status', 'Position', 'Torque(Newtons)', 'Velocity'
'''
with open('C:/Users/wellm/Desktop/dinamometro.txt', 'r', encoding='utf-8') as dinamometro:
    data = csv.DictReader(dinamometro, delimiter=',')

    peak = []
    position = []
    velocity = []

    referência = 0


    for row in data:
        if referência == 0:
            referência = row['Torque(Newtons)']

        if row['Torque(Newtons)'] > referência:
            peak.append(row['Torque(Newtons)'])
            position.append(row['Position'])
            velocity.append(row['Velocity'])

for list_a, list_b, list_c in zip(peak, position, velocity):
    print(list_a, list_b, list_c)
