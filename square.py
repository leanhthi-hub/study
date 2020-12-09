s=int(input())
i=int((s/2)+0.5)
print(i)
j=int((s/2)-0.5)

a=1
ui=list()
q=[0]
counta=1
for i in range(s):
    ui.append(q*s)
ui[j][i-1]=1
print(ui)
while counta<=(s*s):
    ui[j][i-1]=counta
    counta=counta+1
    if (counta%s)!=0:
        j=j-1
        i=i+1
    else:
        i=i+2
    if (i>=s):
        i=i-s
    if (j==-1):
        j=s-1
for i in range(s):
    print(ui[i])




    
