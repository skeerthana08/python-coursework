n=int(input("Enter the no. of messages: "))
chat={}
for i in range(n):
    name,msg=input().split(':')
    if name in chat:
        chat[name].append(msg.strip())
    else:
        chat[name]=[msg.strip()]
while True:
    print("\n1.Count total no. of messages")
    print("2.identify unique users in the chat")
    print("0.Exitn\")
    ch=int(input("enter your choice: "))
    if ch==0:
        break
    elif 1<=ch<=10:
        if ch==1:
            total_msgs=0
            for i in chat:
                total_msgs+=len(chat[i])
            print(f"total no. of messages: {total_msgs}")
        elif ch==2:
            print("unique users in the chat")
            for i key