listData = [3, 2, 0, 2, 7, 23, 0, 7, 4, 0, 45, 7]

def spyGame(list):
    lstExp = [0, 0, 7]

    for elem in list:
        if elem == lstExp[0]:
            lstExp.pop(0)

        if(len(lstExp)==0):
            print('Spy is among us')
            break

spyGame(listData)
