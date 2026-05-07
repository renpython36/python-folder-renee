Amount = int(input("How much,_Amount,do you need"))




FiveHundredPoundBills = Amount//500

print("the No Of 500 pound bills are",FiveHundredPoundBills)

Amount_left = Amount % 500

print("Amount Left is ",Amount_left)

FiftyPoundBills = Amount_left//50

print(FiftyPoundBills )

Amount_left_second = Amount_left % 50 

print("Amount Left is ",Amount_left_second)