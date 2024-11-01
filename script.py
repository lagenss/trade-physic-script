import pyautogui
import time

iterAmount = 1000 #target trade amount
maxErrs = 220 #max amount of possible fails


#don't edit this
i = 0
errs = 0


def oneTradeSending():
    pyautogui.click(540, 63) #click link field
    time.sleep(.400)
    pyautogui.write("https://steamcommunity.com/tradeoffer/new/?partner=XXXXXXXXXXXXXXXXXXXX") #insert trade link
    time.sleep(0.200)
    pyautogui.press('enter') #press enter
    time.sleep(2.400)
    pyautogui.doubleClick(pyautogui.locateCenterOnScreen('banana.png', confidence=0.7)) #select banana
    time.sleep(0.300)
    pyautogui.click(pyautogui.locateCenterOnScreen('checkbox.png', confidence=0.7)) #press checkbox to confirm
    time.sleep(0.300)
    pyautogui.click(pyautogui.locateCenterOnScreen('modal.png', confidence=0.7)) #press modal window shiish
    time.sleep(0.300)
    pyautogui.click(pyautogui.locateCenterOnScreen('makeoffer.png', confidence=0.7)) #press send trade button
    time.sleep(0.300)
    pyautogui.click(pyautogui.locateCenterOnScreen('refresh.png', confidence=0.7)) #press refresh button on sda
    time.sleep(1.600)
    pyautogui.click(pyautogui.locateCenterOnScreen('confirm.png', confidence=0.7)) #press confirm trade on sda
    time.sleep(3.200)

time.sleep(1.000)
while i < iterAmount:
    try:
        oneTradeSending()
        i+=1
        print("Trade number [", end="")
        print(i, end="")
        print("] sent succesfully!")
    except:
        print(f"Trade number [{i+1}] failed! [{errs+1}/{maxErrs}]")
        time.sleep(3.500)
        errs+=1
        if(errs >= maxErrs):
            print("too many fails! ",end="")
            break
print("script finished")
