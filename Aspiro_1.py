anchor =P_i[0]
count =anchor

for x in range(1, len(P_i)):
    if P_i[x]%anchor ==0 and anchor <P_i[x]:
        count=P_i[x]
        anchor=P_i[x]


return count
