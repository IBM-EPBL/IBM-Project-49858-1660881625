import random
temp=list(range(0,1000))
for t in temp:
        value=random.choice(temp)
        if value>=43:
           print("TEMPURATURE IS HIGH!!!",value);
        else:
            print("NORMAL",value);
