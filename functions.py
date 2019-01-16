a1='china'
a2='america'
a3='russia'
a4='united nations'
a5='canada'
my_list=[a1,a2,a3,a4,a5]
def m1(list00):
    print('there are many countries in the list.\n')
    for i in list00:
        print(i)
m1(my_list)
def m2(list01):
    print('there is a list of some countries.\n')
    for i in list01:
        print(i.title())
m2(my_list)
def m3(list02):
    print('items in the list:\n'.title())
    for i in list02:
        print(i.upper())
m3(my_list)
def m4(list03):
    print('items in the list:\n'.upper())
    for i in list03:
        print('(we got)'+i.upper())
m4(my_list)
def m5():
    print('hello,everyone!welcome to here!'.title())
m5()
