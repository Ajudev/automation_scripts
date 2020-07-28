import pyautogui


def screenshot(filename):
    # return pyautogui.position()
    pyautogui.keyDown("alt")
    pyautogui.press("tab")
    pyautogui.keyUp("alt")
    filepath = "D:\\Pictures\\Screenshots\\" + filename
    pyautogui.screenshot(filepath, region=(0, 92, 1893, 926))
    pyautogui.keyDown("alt")
    pyautogui.press("tab")
    pyautogui.keyUp("alt")
    return True


if __name__ == "__main__":
    # val = move_cursor()
    filename = input("Please Enter the file name: ")
    val = screenshot(filename)
    print(val)
