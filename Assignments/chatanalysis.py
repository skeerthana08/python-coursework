n=int(input("Enter no of msgs:"))
chat={}
for i in range(n):
    name,msg=input().split(":",1)
    if name in chat:
        chat[name].append((i,msg.strip()))
    else:
        chat[name]=[(i,msg.strip())]

while True:
    print("\n1. Count total number of messages")
    print("2. Identify unique users in the chat")
    print("3. Count total words in the chat")
    print("4. Calculate average words per message")
    print("5. Find the longest message sent")
    print("6. Find the most active user")
    print("7. Get message count for a specific user")
    print("8. Find most frequently used word by a specific user")
    print("9. Retrieve first and last message by a user")
    print("10. Check if a user is present in the chat")
    print("11. Find commonly repeated words")
    print("12. --- Skipped ---")
    print("13. User with longest average message length")
    print("14. Count how many messages mention a specific user")
    print("15. Remove duplicate messages")
    print("16. Sort messages alphabetically")
    print("17. Extract all questions asked")
    print("18. Calculate reply ratio between two users")
    print("19. Check for deleted messages")
    print("0-Exit")
    
    ch=int(input("Enter your choice:"))
    
    if ch==0:
        break

    elif ch==1:
        total_msgs=0
        for i in chat:
            total_msgs+=len(chat[i])
        print(f'Total number of messages:{total_msgs}')

    elif ch==2:
        print("Unique users in the chat:", set(chat.keys()))

    elif ch==3:
        word_count=0
        for msgs in chat.values():
            for _,msg in msgs:
                word_count+=len(msg.split())
        print("Total words in the chat:", word_count)

    elif ch==4:
        total_words=0
        total_msgs=0
        for msgs in chat.values():
            total_msgs+=len(msgs)
            for _,msg in msgs:
                total_words+=len(msg.split())
        if total_msgs==0:
            print("Average words per message: 0")
        else:
            avg=total_words/total_msgs
            print("Average words per message:", round(avg,2))

    elif ch==5:
        longest=""
        for name,msgs in chat.items():
            for _,msg in msgs:
                if len(msg)>len(longest):
                    longest=f"{name}: {msg}"
        print("Longest message:", longest)

    elif ch==6:
        max_user=""
        max_count=0
        for name,msgs in chat.items():
            if len(msgs)>max_count:
                max_count=len(msgs)
                max_user=name
        print(f"Most active user: {max_user} ({max_count} messages)")

    elif ch==7:
        uname=input("Enter username: ")
        if uname in chat:
            print(f"Messages sent by {uname}: {len(chat[uname])}")
        else:
            print("User not found.")

    elif ch==8:
        uname=input("Enter username: ")
        if uname in chat:
            word_freq={}
            for _,msg in chat[uname]:
                for word in msg.lower().split():
                    word_freq[word]=word_freq.get(word,0)+1
            if word_freq:
                max_word=max(word_freq,key=word_freq.get)
                print(f'Most frequent word used by {uname}: "{max_word}"')
            else:
                print("No words found.")
        else:
            print("User not found.")

    elif ch==9:
        uname=input("Enter username: ")
        if uname in chat:
            msgs=sorted(chat[uname])
            print(f"First message by {uname}: \"{uname}: {msgs[0][1]}\"")
            print(f"Last message by {uname}: \"{uname}: {msgs[-1][1]}\"")
        else:
            print("User not found.")

    elif ch==10:
        uname=input("Enter username: ")
        if uname in chat:
            print(f"User '{uname}' is present in the chat.")
        else:
            print(f"User '{uname}' not found in the chat.")

    elif ch==11:
        all_words={}
        for msgs in chat.values():
            for _,msg in msgs:
                for word in msg.lower().split():
                    all_words[word]=all_words.get(word,0)+1
        repeated={word for word in all_words if all_words[word]>1}
        print("Common repeated words:", repeated)

    elif ch==13:
        max_avg=0
        user=""
        for name in chat:
            total_words=sum(len(msg.split()) for _,msg in chat[name])
            count=len(chat[name])
            avg=total_words/count if count else 0
            if avg>max_avg:
                max_avg=avg
                user=name
        print(f"User with longest average message: {user} (avg {round(max_avg,2)} words)")

    elif ch==14:
        uname=input("Enter name to check mentions: ").lower()
        mention_count=0
        for msgs in chat.values():
            for _,msg in msgs:
                if uname in msg.lower():
                    mention_count+=1
        print(f"Messages mentioning '{uname}': {mention_count}")

    elif ch==15:
        seen=set()
        unique=[]
        for msgs in chat.values():
            for _,msg in msgs:
                if msg not in seen:
                    seen.add(msg)
                    unique.append(msg)
        print("Unique messages count:", len(unique))
        for m in unique:
            print("-", m)

    elif ch==16:
        all_msgs=[]
        for name,msgs in chat.items():
            for _,msg in msgs:
                all_msgs.append(f"{name}: {msg}")
        all_msgs.sort()
        print("Messages sorted A-Z:")
        for m in all_msgs:
            print(m)

    elif ch==17:
        print("Questions in chat:")
        for name,msgs in chat.items():
            for _,msg in msgs:
                if '?' in msg:
                    print(f"{name}: {msg}")

    elif ch==18:
        u1=input("Enter first user: ")
        u2=input("Enter second user: ")
        msgs=[]
        for name,msgs_list in chat.items():
            for index,msg in msgs_list:
                msgs.append((index,name,msg))
        msgs.sort()
        replies=0
        for i in range(1,len(msgs)):
            if msgs[i-1][1]==u1 and msgs[i][1]==u2:
                replies+=1
        print(f"Reply ratio from {u2} to {u1}: {replies} replies")

    elif ch==19:
        deleted=0
        for msgs in chat.values():
            for _,msg in msgs:
                if msg.lower()=="this message was deleted":
                    deleted+=1
        print("Deleted messages found:", deleted)

    else:
        print("Invalid choice.")