you = input("")


while "pi" in you or "ka" in you or "chu" in you:
    you = you.replace("pi","") 
    you = you.replace("ka","")
    you = you.replace("chu","") 

if you == "" :
    print("YES")
else :
    print("NO")