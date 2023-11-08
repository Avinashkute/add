with open("C:\\Users\Admin\Desktop\input\\emp_data.txt.txt","r") as fp:
    # fetch data
    data=fp.readlines()
    l1=[]
    for i in data:
        d=i.split()
        name=d[0].split('(')[0]+' '+d[1]
        sal=int(d[0].split('(')[-1][:-1])
        hike=int(d[-2][:-1])
        s=f'Salary of {name} will be {sal+sal*(hike/100)}'
        l1.append(s)
with open(f"C:\\Users\Admin\Desktop\input\\slary.txt",'w') as fp:
    fp.writelines(l1)


    # print(data)
