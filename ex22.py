# coding=utf-8
def conclusion(*args): # Give a lot of arguments(*args)
    a,b,c,d,e,f,g,h=args 
    print("1.%s"%a,"2.%s"%b,"3.%s"%c)
    print("4.%s"%d,"5.%s"%e,"6.%s"%f)
    print("7.%s"%g,"8.%s"%h)
def sample():
    print("Hello,world!")
    file_again=input("filename: ")
    file_again1=open(file_again,'r')
    print(file_again1.read())
    file_again1.close()
def final_conclusion():
    a="powershell"
    b="print"
    c="variable"
    d="import module"
    e="function"
    f="open file"
    g="format string"
    h="math"
    conclusion(a,b,c,d,e,f,g,h)
    sample()
hello=input("Type:")
hello_again=open(hello,'r')
print(hello_again.read())
hello_again.close()
print("Take a while and think about something, and then type RETURN.")
input("......")
final_conclusion()

print("Here we got something:\n")
print("""
\t# 1 from sys import argv (import module)
\t# 2 script, a,s,d=argv (unpack)
\t# 3 %s %d %r %t (format strings)
\t# 4 \_ \_n \_\ \_t \_' \_" (escape_consequences,to avoid something unexpected,here we add "_")
\t# 5  + - * / >= <= == (math)
\t# 6 open print input def (related to functions)
""")

