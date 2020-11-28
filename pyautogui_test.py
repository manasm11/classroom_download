import pyautogui as pg
from time import sleep
import hashlib
import threading
import binascii
# print(pg.KEY_NAMES)
# print(hashlib.sha512(b"BY").hexdigest())
# print(binascii.hexlify(hashlib.pbkdf2_hmac("sha512", b"PASSWORD123", b"MANAS", 100000)))
# username = ""
# password = ""


# def get_creds():
#     global username, password
#     username = pg.prompt(
#         text="Enter NALANDA username",
#         title="Username",
#         default="@pilani.bits-pilani.ac.in"
#     )

#     password = pg.password(
#         text="Enter NALANDA password",
#         title="Password"
#     )

# t1 = threading.Thread(target=get_creds)
# t1.start()

# pg.hotkey("winleft")
# sleep(1)
# # pg.click(x=600, y=64) # Got this position by pg.diplayMousePosition()
# pg.typewrite("brave\n")
# sleep(1)
# pg.click()
# pg.hotkey("ctrl", "t")
# sleep(1)

# pg.hotkey("winleft")
# sleep(1)
# pg.typewrite("file\n", interval=0.1)
# pg.sleep(1)
# backup_location = (316, 103)
# pg.doubleClick(backup_location)
# pg.displayMousePosition()
# sleep(0.5)
# pg.hotkey("ctrl", "t")
# sleep(1)
# pg.click(pg.locateCenterOnScreen("gmail.png"))
# pg.typewrite("classroom.google.com\n")
# sleep(5)
# coordinates = pg.locateCenterOnScreen("gtor.png")
# pg.click(coordinates)

# coordinates = pg.locateCenterOnScreen("github.png")
# print(coordinates)
# pg.click(coordinates)


# pg.click()
# pg.moveRel(100, 100, 0.2) # To move
# pg.dragRel(100, 100, 0.2) # To drag
# pg.typewrite("HELLO !!!", 0.1) # To type

# Code to do 1+1 in calculator
# sleep(2)
# pg.click(pg.locateCenterOnScreen("1_calc.png"))
# sleep(0.1)  # Don't know why but this delay is needed for it to work correctly
# pg.click(pg.locateCenterOnScreen("plus_calc.png"))
# sleep(0.1)
# pg.click(pg.locateCenterOnScreen("1_calc.png"))
# sleep(0.1)
# pg.click(pg.locateCenterOnScreen("eq_calc.png"))
# sleep(0.1)

# CONTROLLING MOUSE
# To stop pyautogui immediately, move mouse to top-left corner (when FAILSAFE is enabled)
# pg.FAILSAFE = True
# Position of mouse is given as (X,Y) pair.
# Position depends on monitor resolution also.
# To view monitor resolution, print(pg.size())
# print(pg.size()) # This will be maximum values of x and y

# To get mouse position, print(pg.position())
# print(pg.position())

# To view live location of mouse
# pg.displayMousePosition()

# To scroll
# pg.scroll(-2)

# CONTROLLING KEYBOARD
# To view all available keys,
# print(pg.KEY_NAMES)

pg.FAILSAFE = True
# Code to open brave browser
# To press any key


# pg.typewrite("https://nalanda.bits-pilani.ac.in/login/index.php\n")
# pg.sleep(2)
# pg.click(pg.locateCenterOnScreen("username_input.png"))
# t1.join()
# pg.typewrite(username, interval=0.1)
# pg.click(pg.locateCenterOnScreen("password_input.png"))
# pg.typewrite(password+"\n", interval=0.1)

# open_nalanda()
# MESSAGE BOX
# Try to run these one-by-one
# input_ = pg.prompt(text="Please enter you username", title="Username", default="HOMO SEPIAN") # Returns None if cancelled and empty string if just pressed ok
# input_ = pg.password(text="Enter your password", title="Passwors", mask="#")
# input_ = pg.alert(text="Your program ran successfully", title="SUCCESS MESSAGE", button="Okies")
# input_ = pg.confirm(text="What do you want to open ?", title="Browser Tab", buttons=[
#     "Youtube",
#     "Gmail",
#     "Drive",
#     "Meet",
#     "Facebook",
#     "Instagram",
# ])
# print(input_)
