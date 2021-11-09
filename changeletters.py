a = input()
a1 = a[a.find('h')+1:a.rfind('h')] #Нахождение второй и последней h
a1 = a1.replace('h','H') #замена
print(a[:a.find('h')+1] + a1 + a[a.rfind('h'):])
