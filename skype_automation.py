import pyautogui
import time
import ctypes


def skype_automation(option) -> None:
    """
    Function designed to automate daily skype tasks with options as follows:
    Option 1: To move cursor to keep skype status active until and unless user manually kills the script
    Option 2: To change skype status to Active and change mood message to work from home
    Option 3: To change skype status to Away and change mood message to out for lunch
    Option 4: To change skype status to Away and clear mood message
    Option 5: To change skype status to Active and clear mood message
    """
    # pyautogui.press(["ctrl", "p"])
    # return pyautogui.position()
    # i = 0
    if option == 1:
        while True:
            # pyautogui.moveTo(923, 514, duration=2)
            # pyautogui.click()
            # * Switch to skype tab
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            pyautogui.keyUp("alt")
            # * Open Conversation profile
            pyautogui.keyDown("ctrl")
            pyautogui.press("p")
            pyautogui.keyUp("ctrl")
            # * Cloe conversation profile
            pyautogui.press("esc")
            # * Switch back to previous application
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            pyautogui.keyUp("alt")

            # pyautogui.moveTo(3504, 446, duration=2)
            # pyautogui.click()
            time.sleep(30)  # * Sleep for 30 seconds and start process again
    elif option == 2:
        # return pyautogui.position()
        pyautogui.moveTo(33, 63, duration=1)
        pyautogui.click()
        pyautogui.moveTo(46, 313, duration=1)
        pyautogui.click()
        # * move to position the cursor on top of active
        pyautogui.moveTo(47, 323, duration=1)
        pyautogui.click()  # * click on active
        pyautogui.moveTo(33, 63, duration=1)
        pyautogui.click()
        pyautogui.moveTo(58, 388, duration=1)
        pyautogui.click()
        # * move to position the cursor on the scroll bar
        pyautogui.moveTo(409, 392, duration=1)
        # * click and drag the scroll bar to the end in line with WFH mood message
        pyautogui.dragTo(407, 798, 2, button='left')
        # * move to position the cursor on top of WFH mood message
        pyautogui.moveTo(89, 808, duration=1)
        pyautogui.click()  # * click on WFH mood message
        pyautogui.click()  # * click on WFH mood message
        pyautogui.moveTo(364, 127, duration=1)
        pyautogui.click()
        pyautogui.press("esc")
        return True
    elif option == 3:
        # return pyautogui.position()
        # * move to position the cursor on the profile icon at top left corner of skype
        pyautogui.moveTo(33, 63, duration=1)
        pyautogui.click()  # * click on profile icon
        # * move to position the cursor on top of status
        pyautogui.moveTo(46, 313, duration=1)
        pyautogui.click()  # * click on status
        # * move to position the cursor on top of away
        pyautogui.moveTo(64, 359, duration=1)
        pyautogui.click()  # * click on away
        # * move to position the cursor on the profile icon at top left corner of skype
        pyautogui.moveTo(33, 63, duration=1)
        pyautogui.click()  # * click on profile icon
        # * move to position the cursor on top of mood message
        pyautogui.moveTo(58, 388, duration=1)
        pyautogui.click()  # * click on mood message selector
        # * move to position the cursor on top of out for lunch mood message
        pyautogui.moveTo(62, 450, duration=1)
        pyautogui.click()  # * click on the message to set mood
        # * move to position the cursor on top of done button
        pyautogui.moveTo(364, 127, duration=1)
        pyautogui.click()  # * click on done button
        pyautogui.press("esc")  # * press esc key
        ctypes.windll.user32.LockWorkStation()  # * Used to lock windows desktop
        return True
    elif option == 4:
        # return pyautogui.position()
        pyautogui.moveTo(33, 63, duration=1)
        pyautogui.click()
        pyautogui.moveTo(46, 313, duration=1)
        pyautogui.click()
        pyautogui.moveTo(64, 359, duration=1)
        pyautogui.click()
        pyautogui.moveTo(33, 63, duration=1)
        pyautogui.click()
        # * move to position cursor on clear mood message button
        pyautogui.moveTo(391, 389, duration=1)
        pyautogui.click()  # * click on clear mood message button
        pyautogui.press("esc")
        return True
    elif option == 5:
        # return pyautogui.position()
        pyautogui.moveTo(33, 63, duration=1)
        pyautogui.click()
        pyautogui.moveTo(46, 313, duration=1)
        pyautogui.click()
        pyautogui.moveTo(47, 323, duration=1)
        pyautogui.click()
        pyautogui.moveTo(33, 63, duration=1)
        pyautogui.click()
        pyautogui.moveTo(391, 389, duration=1)
        pyautogui.click()
        pyautogui.press("esc")
        return True
    else:
        return "Incorrect Option"
        # i += 1
    # return True
    # return pyautogui.size()  # * Used to find out size of screen


if __name__ == "__main__":
    option = int(input("Please Enter 1 to move cursor, 2 to change status to online and WFH, 3 to change status to away and going for lunch, 4 to change status to away, 5 to change status to active: "))
    val = skype_automation(option)
    print(val)
