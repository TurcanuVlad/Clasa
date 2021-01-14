with open('sir de caractere.txt', 'r') as f:
    n=f.readline()
a=0
b=0
c=0
d=0
for i in n:
    if ord(i) in range (65,91):
        a+=1
for i in n:
    if ord (i) in range (97,123):
        b+=1
for i in n:
    if ord(i) in range (49,58):
        c+=1
for i in n:
    if ord(i) in range (33,42):
        d+=1
with open('Majuscule.txt', 'w') as f:
    f.write(str(a))
with open('Minuscule.txt', 'w') as f:
    f.write(str(b))
with open('Cifre.txt', 'w') as f:
    f.write(str(c))
with open('Semne.txt', 'w') as f:
    f.write(str(d))
