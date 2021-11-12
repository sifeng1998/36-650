def delete_keys(keyList,dictionary):
    for key in keyList:
        if key in dictionary:
            dictionary.pop(key)
    return dictionary

dict = {"firstName": "Mohamed", "lastName": "Farag", "birthYear": 1990, "nationality": "Egyptian"}
a = delete_keys(["lastName","birthYear"],dict)
print(a)