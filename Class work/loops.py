#login 

pin = 1234
while True:
    ent_pin=int(input("0-Exit:"))
    if pin==ent_pin:
        print("login successful")
        break
    else:
        print("invalid login. try again!!!")


#chat
n=int(input("Enter the no. of messages: "))
chat={}
for i in range(n):
    name,msg=input().split(':')
    if name in chat:
        chat[name].append(msg.strip())
    else:
        chat[name]=[msg.strip()]
print(chat)
    

#