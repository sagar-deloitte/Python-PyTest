sampleDict = {

    "name": "Kelly",

    "age": 25,

    "salary": 8000,

    "city": "New york"

}
for keys, values in sampleDict.items():
    if keys == 'city':
        keys = 'location'
    print(keys,": ",values)
