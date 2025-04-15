#نمرات درسی یک محصل 
# از float برای اعداد اعشاری احتمالی استفاده میکنیم
nomre1 = float(input("14"))
nomre2 = float(input("16.5"))
nomre3 = float(input("18"))
nomre4 = float(input("13.75"))
nomre5 = float(input("19"))
nomre6 = float(input("10"))

#با استفاده از average میانگین دروس را میگیریم

average = (nomre1+nomre2+nomre3+nomre4+nomre5+nomre6) / 6

#معدل را پرینت میگیرم.
print("معدل شما:", average)

#شروط 

if average >=18:
    print("شما برنده پلی استیشن شدید")
elif average >=16:
    print("شما برنده دوچرخه شدید")
else:
    print("شرمنده جایزه ای نداریم")        