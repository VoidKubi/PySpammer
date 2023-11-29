import time
import pyautogui as pygui


print("Spammer by @VoidKubi")
print(" ")

co = input("Jakie słowo? ")
ile = int(input("Ile razy? "))

print("Spam zacznie się za 5 sekund.")

time.sleep(5)

for i in range(ile):
    pygui.typewrite(co)
    pygui.press("enter")

end = input("Wciśnij enter aby zakończyć ")
