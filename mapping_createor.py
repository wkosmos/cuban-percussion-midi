

filepath = 'mapping.json'

with open(filepath, 'w') as f:

    f.write('{\n')

    for i in range(127):
        f.write(f'\'\' : {i},\n')
    
    f.write('128 : \'\'\n}')
    
