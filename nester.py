my_list=['asia','europe',['china',['shanghai','beijing','shenzhen','guangzhou']]]
for i in my_list:
    if isinstance(i,list):
        for j in i:
            if isinstance(j,list):
                for k in j:
                    print(k)
            else:
                print(j)
    else:
        print(i)