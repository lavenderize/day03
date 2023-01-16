# 5.8

animals = 'duck', 'gourd', 'spitz'

# for i in range(0, 3):
#    upper = animals[i].capitalize()
#    statement = "%sy Mc%sface"%(upper, upper)
#    print(statement)

for i in range(0, 3):
    upper = animals[i].capitalize()
    statement = f'{upper}y Mc{upper}face'

    print(statement)