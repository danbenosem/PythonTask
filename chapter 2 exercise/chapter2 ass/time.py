user_seconds= int(input("Enter the seconds:"))

hours =  user_seconds// 3600

remain_seconds= user_seconds % 3600

minutes= remain_seconds // 60


seconds = minutes % 60


print(hours,"hours",minutes,"minutes",seconds,"seconds")
