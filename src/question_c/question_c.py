#write functions here, don't add input('') statements here!

def get_bonus_pay_amount(sales):
    bonus = ""
    if (sales >=0 and sales <= 499):
        bonus = sales * .05
    elif (sales >=500 and sales <= 999):
        bonus = sales * .06
    elif (sales >= 1000 and sales <= 1499):
        bonus = sales * .07
    elif (sales >= 1500 and sales <= 1999):
        bonus = sales * .08
    elif (sales <0 or sales >= 2000):
        return "Invalid Argument"
    return bonus