num=int(input())
십의자리 = num//10
일의자리 = num % 10

if 십의자리 % 3 ==0 and 일의자리 % 3 ==0:
    print("**")
elif 십의자리 % 3 ==0 or 일의자리 % 3 ==0:
    print("??")
else:
    print(">>")
