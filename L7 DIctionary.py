data = {1: 'SADI', 2: 'ADNAN', 3: 'ABDULLAH'}
print(data)
print(data[2])
print(data.get(3)) # will not return error
print(data.get(3, 'not found'))

keys = ['nsu', 'brac', 'aust']
values = ['BBA', 'CSE', 'Mechanical']

data = dict(zip(keys, values))
data['monika'] = 'CS'

del data['brac']
