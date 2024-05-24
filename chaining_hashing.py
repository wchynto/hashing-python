def remainderFunction(data:int, divisor:int):
    return data % divisor

def createHashTable(length:int):
    return [None] * length

def putData(data:int, hashTable:list):
    for i in range(len(data)):
        index = remainderFunction(data[i], len(hashTable))
        if hashTable[index] == None:
            hashTable[index] = [data[i]]
        else: 
            hashTable[index].append(data[i])
    return hashTable

def searchHash(data:int, hashTable:list):
    hashValue = remainderFunction(data, len(hashTable))
    for i in hashTable[hashValue]:
        while i == data:
            return True
    return False

lst = [54, 26, 93, 17, 77, 31, 44, 55, 20]

hashTable = createHashTable(11)

hashTable = putData(lst, hashTable)

print(hashTable)

print(searchHash(44, hashTable))