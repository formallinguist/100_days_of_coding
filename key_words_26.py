def person(name,**data):
    for i,j in data.items():
        print(i,j)
    
person("Ravi",age = 26,place = "guntur", study = "linguistics")

