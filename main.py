import keyboard
import pyautogui

message_toSend = pyautogui.prompt("Enter The message you want to spam")

text_input = pyautogui.locateCenterOnScreen("text_input_messenger.png")
pyautogui.moveTo(text_input)
pyautogui.click()

try:
    while True:
        if keyboard.is_pressed("esc"):
            print("terminated")
            break
        pyautogui.write(message_toSend)
        pyautogui.hotkey("enter")

except KeyboardInterrupt:
    print("ending Program")