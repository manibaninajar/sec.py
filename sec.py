#نمرات درسی یک محصل 
# از int برای اعداد استفاده میکنیم
nomre1 = int(input("14"))
nomre2 = int(input("16.5"))
nomre3 = int(input("18"))
nomre4 = int(input("13.75"))
nomre5 = int(input("19"))
nomre6 = int(input("10"))

#با استفاده از average میانگین دروس را میگیریم

average = (nomre1+nomre2+nomre3+nomre4+nomre5+nomre6) / 6

#معدل را پرینت میگیرم.
print("معدل شما:", average)

#شروط 

if 18 <= average <= 20:
    print("شما برنده پلی استیشن شدید")
elif 16 <= average <= 18:
    print("شما برنده دوچرخه شدید")
else:16 > average
    print("شرمنده جایزه ای نداریم")        
