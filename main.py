import time

while True:
    print("\npress 1 to start your test\npress 2 to exit")
    op=int(input())

    try:
        if op==1:           
            er=0
            def error():
                try:
                    for i in range(len(ans)):
                        if ans[i]!=sample[i]:
                            er+=1
                        if i==len(ans)-1:
                            print("error=",er)
                        
                except:
                    pass            

            def speed():
                try:
                    print(int(len(ans)/((t2-t1)*60)),"words per minute\n")
                except:
                    pass 


            print("you will have to type the given paragraph with the least amount of error possible\npress 1 when you're ready\n\n")
            rea=int(input())
            try:
                if rea==1:
                    sample="\nOne morning my friend and I were thinking about how we could plan our summer break away from school Driving from our own state to several nearby states would help to expand our limited funds Inviting six other friends to accompany us would lower our car expenses Stopping at certain sites would also help us stretch our truly limited travel budget. Yesterday I engaged in an interesting and enlightening discussion about finances I found it difficult to imagine that during my lifetime I might well earn at least one-half million dollars It is also possible that I might spend as much as one-half million during the same period The really difficult thing for me to do will be to save more of the half-million than I spend Thinking about today's high cost of living makes this seem an impossible task for most Last week I asked a friend to talk with me and a girl-friend about college Our friend is the Dean of Women at a nearby college The Dean and her staff spend much of their time talking to students who plan to go to college The first thing she said was to work very hard each day in high school Good grades are most important for being accepted Being on time for classes and having a good view toward all phases of the school life are two other things to remember.\n\n"
                    print(sample)
                    sample=sample.lower()
                    sample=sample.split()
                    t1=time.time()                 
                    ans=input()
                    ans=ans.split("")
                    t2=time.time()
                    error()
                    speed()
            except:
                pass                    

        elif op==2:
            break
        
    except:
        print("oops! i didn't get it")
