data = {1:"RAVI",2:"KIRAN",3:"NAVEEN"}

print(data)

data[3]

data.get(1)

print(data.get(1))

#creating a dictionary out of lists.
keys = ['Navin','Kiran','Harsh']

values = ['Python','java','html']

data = dict(zip(keys,values))

print(data)

data['divya'] = ['cs']

print(data)

prog = {'JS':'Atom','cs':'vs','python':['Pycharm','Sublime'],'java':{'jse':'netbeans','jee':'eclipse'}}

print(prog['JS'])

print(prog['python'])

print(prog['python'][1])

print(prog['java'])

print(prog['java']['jee'])







