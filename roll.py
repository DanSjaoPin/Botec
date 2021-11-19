import random

def Roll():
    dice_value = random.randrange(1, 7)
    dice = ''
    if dice_value == 1:
        dice = """— — — \n—  o  — \n— — — """
    elif dice_value == 2:
        dice = """o  — — \n— — — \n— —  o"""
    elif dice_value == 3:
        dice = """— — o\n— o — \no — — """
    elif dice_value == 4:
        dice = """o — o\n— — — \no — o"""
    elif dice_value == 5:
        dice = """o — o\n— o — \no — o"""
    elif dice_value == 6:
        dice = """o — o\no — o\no — o"""
    return(dice)