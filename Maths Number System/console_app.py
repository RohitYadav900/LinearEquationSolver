sum_num = int(input("Type the sum of two digit number: "))
diff = int(input("Type the difference between the digit of two digit number: "))

b=(sum_num-diff*11)/22

reslt_1 =(b+diff)*10+b

reslt_2 =(b*10)+b+diff
print("Your first numbers is {}.".format(round(reslt_1)),
                "\nYour second number is {}.".format(round(reslt_2)))
input("")
