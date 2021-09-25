def on_keypad_click():
    global DriverCommand, NUMFLASH
    keyboard.type("t")
    light.set_all(0x000000)
    light.set_pixel_color(27, 0xffffff)
    pause(100)
    keyboard.type("!")
    keyboard.type("clear")
    DriverCommand = 1
    NUMFLASH = 1
matrixKeypad.keypad.on_event(3, 3, MatrixKeypadButtonEvent.CLICK, on_keypad_click)

def on_keypad_click2():
    global Tire
    if Tire == 0:
        Tire = 1
        tyre()
    else:
        Tire = 0
        tyre()
matrixKeypad.keypad.on_event(1, 2, MatrixKeypadButtonEvent.CLICK, on_keypad_click2)

def on_keypad_click3():
    keyboard.type("t")
    light.set_pixel_color(9, 0xffff00)
    pause(100)
    keyboard.type("Pitting In")
    pause(100)
    enter()
matrixKeypad.keypad.on_event(1, 1, MatrixKeypadButtonEvent.CLICK, on_keypad_click3)

def on_keypad_click4():
    global DriverCommand, NUMFLASH
    keyboard.type("t")
    light.set_all(0x000000)
    light.set_pixel_color(28, 0xffffff)
    pause(100)
    keyboard.type("!")
    keyboard.type("waveby")
    DriverCommand = 1
    NUMFLASH = 1
matrixKeypad.keypad.on_event(4, 3, MatrixKeypadButtonEvent.CLICK, on_keypad_click4)

def on_keypad_click5():
    global QwkRpr
    if QwkRpr == 0:
        QwkRpr = 1
        QwkR()
    else:
        QwkRpr = 0
        QwkR()
matrixKeypad.keypad.on_event(0, 2, MatrixKeypadButtonEvent.CLICK, on_keypad_click5)

def on_keypad_click6():
    keyboard.type("t")
    light.set_pixel_color(24, 0xffff00)
    pause(100)
    keyboard.type("!yellow")
    pause(100)
    enter()
matrixKeypad.keypad.on_event(0, 3, MatrixKeypadButtonEvent.CLICK, on_keypad_click6)

def on_keypad_up():
    global NUMFLASH
    if DriverCommand == 1:
        NUMFLASH = 0
        pause(100)
        light.set_pixel_color(15, 0x00ffff)
        keyboard.type("0")
        light.set_pixel_color(7, 0xffff00)
matrixKeypad.keypad.on_event(7, 1, MatrixKeypadButtonEvent.UP, on_keypad_up)

def on_keypad_click7():
    keyboard.type("t")
    light.set_pixel_color(1, 0xffff00)
    pause(100)
    keyboard.type("Pitting Out")
    pause(100)
    enter()
matrixKeypad.keypad.on_event(1, 0, MatrixKeypadButtonEvent.CLICK, on_keypad_click7)

def on_keypad_up2():
    global NUMFLASH
    if DriverCommand == 1:
        NUMFLASH = 0
        pause(100)
        light.set_pixel_color(12, 0xffffff)
        keyboard.type("2")
        light.set_pixel_color(7, 0x00ffff)
matrixKeypad.keypad.on_event(4, 1, MatrixKeypadButtonEvent.UP, on_keypad_up2)

def on_keypad_click8():
    keyboard.type("t")
    light.set_pixel_color(26, 0xffff00)
    pause(100)
    keyboard.type("!")
    keyboard.type("restart double")
    pause(100)
    enter()
matrixKeypad.keypad.on_event(2, 3, MatrixKeypadButtonEvent.CLICK, on_keypad_click8)

def on_keypad_up3():
    global NUMFLASH
    if DriverCommand == 1:
        NUMFLASH = 0
        pause(100)
        light.set_pixel_color(14, 0xffffff)
        keyboard.type("8")
        light.set_pixel_color(7, 0x00ffff)
matrixKeypad.keypad.on_event(6, 1, MatrixKeypadButtonEvent.UP, on_keypad_up3)

def on_keypad_click9():
    keyboard.type("t")
    light.set_pixel_color(25, 0xffff00)
    pause(100)
    keyboard.type("!")
    keyboard.type("restart single")
    pause(100)
    enter()
matrixKeypad.keypad.on_event(1, 3, MatrixKeypadButtonEvent.CLICK, on_keypad_click9)

def on_keypad_click10():
    keyboard.type("t")
    light.set_pixel_color(11, 0xffff00)
    pause(100)
    keyboard.type("!")
    keyboard.type("advance")
    pause(100)
    enter()
matrixKeypad.keypad.on_event(3, 1, MatrixKeypadButtonEvent.CLICK, on_keypad_click10)

def on_keypad_click11():
    global DriverCommand, NUMFLASH
    light.set_pixel_color(7, 0xffffff)
    DriverCommand = 0
    NUMFLASH = 0
    enter()
matrixKeypad.keypad.on_event(7, 0, MatrixKeypadButtonEvent.CLICK, on_keypad_click11)

def on_keypad_click12():
    keyboard.type("t")
    light.set_pixel_color(3, 0xffff00)
    pause(100)
    keyboard.type("!")
    keyboard.type("help")
    pause(100)
    enter()
matrixKeypad.keypad.on_event(3, 0, MatrixKeypadButtonEvent.CLICK, on_keypad_click12)

def on_keypad_up4():
    global NUMFLASH
    if DriverCommand == 1:
        NUMFLASH = 0
        pause(100)
        light.set_pixel_color(21, 0xffffff)
        keyboard.type("4")
        light.set_pixel_color(7, 0x00ffff)
matrixKeypad.keypad.on_event(5, 2, MatrixKeypadButtonEvent.UP, on_keypad_up4)

def tyre():
    if Tire == 1:
        light.set_pixel_color(17, 0xffff00)
        pause(100)
        keyboard.type("t")
        pause(500)
        keyboard.type("#")
        keyboard.type("lf rf lr rr")
        keyboard.function_key(KeyboardFunctionKey.ENTER, KeyboardKeyEvent.PRESS)
        keyboard.function_key(KeyboardFunctionKey.ESC, KeyboardKeyEvent.PRESS)
    else:
        light.set_pixel_color(17, 0x000000)
        pause(100)
        keyboard.type("t")
        pause(500)
        keyboard.type("#")
        keyboard.type("!cleartires")
        keyboard.function_key(KeyboardFunctionKey.ENTER, KeyboardKeyEvent.PRESS)
        keyboard.function_key(KeyboardFunctionKey.ESC, KeyboardKeyEvent.PRESS)

def on_keypad_click13():
    keyboard.type("t")
    light.set_pixel_color(0, 0xffff00)
    pause(100)
    keyboard.type("Pass Right")
    pause(100)
    enter()
matrixKeypad.keypad.on_event(0, 0, MatrixKeypadButtonEvent.CLICK, on_keypad_click13)

def enter():
    keyboard.function_key(KeyboardFunctionKey.ENTER, KeyboardKeyEvent.PRESS)
    pause(100)
    keyboard.function_key(KeyboardFunctionKey.ESC, KeyboardKeyEvent.PRESS)
    pause(100)
    light.set_all(0x000000)
    pause(500)
    light.set_all(0xffffff)

def on_keypad_click14():
    light.set_pixel_color(18, 0xffff00)
    pause(100)
    keyboard.type("t")
    pause(500)
    keyboard.type("#")
    keyboard.type("fuel 2g")
    pause(100)
    enter()
matrixKeypad.keypad.on_event(2, 2, MatrixKeypadButtonEvent.CLICK, on_keypad_click14)

def on_keypad_up5():
    global NUMFLASH
    if DriverCommand == 1:
        NUMFLASH = 0
        pause(100)
        light.set_pixel_color(13, 0xffffff)
        keyboard.type("5")
        light.set_pixel_color(7, 0x00ffff)
matrixKeypad.keypad.on_event(5, 1, MatrixKeypadButtonEvent.UP, on_keypad_up5)

def on_keypad_up6():
    global NUMFLASH
    if DriverCommand == 1:
        NUMFLASH = 0
        pause(100)
        light.set_pixel_color(5, 0xffffff)
        keyboard.type("6")
        light.set_pixel_color(7, 0x00ffff)
matrixKeypad.keypad.on_event(5, 0, MatrixKeypadButtonEvent.UP, on_keypad_up6)

def on_keypad_up7():
    global NUMFLASH
    if DriverCommand == 1:
        NUMFLASH = 0
        pause(100)
        light.set_pixel_color(4, 0xffffff)
        keyboard.type("3")
        light.set_pixel_color(7, 0x00ffff)
matrixKeypad.keypad.on_event(4, 0, MatrixKeypadButtonEvent.UP, on_keypad_up7)

def on_keypad_click15():
    global DriverCommand, NUMFLASH
    keyboard.type("t")
    light.set_all(0x000000)
    light.set_pixel_color(29, 0xffffff)
    pause(100)
    keyboard.type("!")
    keyboard.type("eol")
    DriverCommand = 1
    NUMFLASH = 1
matrixKeypad.keypad.on_event(5, 3, MatrixKeypadButtonEvent.CLICK, on_keypad_click15)

def on_keypad_click16():
    global DriverCommand, NUMFLASH
    keyboard.type("t")
    light.set_all(0x000000)
    light.set_pixel_color(19, 0xffffff)
    pause(100)
    keyboard.type("!")
    keyboard.type("remove")
    DriverCommand = 1
    NUMFLASH = 1
matrixKeypad.keypad.on_event(3, 2, MatrixKeypadButtonEvent.CLICK, on_keypad_click16)

def QwkR():
    if QwkRpr == 1:
        light.set_pixel_color(16, 0xffff00)
        pause(100)
        keyboard.type("t")
        pause(500)
        keyboard.type("#")
        keyboard.type("fr")
        keyboard.function_key(KeyboardFunctionKey.ENTER, KeyboardKeyEvent.PRESS)
        keyboard.function_key(KeyboardFunctionKey.ESC, KeyboardKeyEvent.PRESS)
    else:
        light.set_pixel_color(16, 0x000000)
        pause(100)
        keyboard.type("t")
        pause(500)
        keyboard.type("#")
        keyboard.type("!fr")
        keyboard.function_key(KeyboardFunctionKey.ENTER, KeyboardKeyEvent.PRESS)
        keyboard.function_key(KeyboardFunctionKey.ESC, KeyboardKeyEvent.PRESS)

def on_keypad_click17():
    global DriverCommand, NUMFLASH
    light.set_pixel_color(23, 0xffffff)
    keyboard.function_key(KeyboardFunctionKey.ESC, KeyboardKeyEvent.PRESS)
    DriverCommand = 0
    NUMFLASH = 0
    pause(250)
    light.set_all(0x000000)
    enter()
matrixKeypad.keypad.on_event(7, 2, MatrixKeypadButtonEvent.CLICK, on_keypad_click17)

def on_keypad_click18():
    keyboard.type("t")
    light.set_pixel_color(8, 0xffff00)
    pause(100)
    keyboard.type("Pass Left")
    pause(100)
    enter()
matrixKeypad.keypad.on_event(0, 1, MatrixKeypadButtonEvent.CLICK, on_keypad_click18)

def on_keypad_up8():
    global NUMFLASH
    if DriverCommand == 1:
        NUMFLASH = 0
        pause(100)
        light.set_pixel_color(22, 0xffffff)
        keyboard.type("7")
        light.set_pixel_color(7, 0x00ffff)
matrixKeypad.keypad.on_event(6, 2, MatrixKeypadButtonEvent.UP, on_keypad_up8)

def on_keypad_up9():
    global NUMFLASH
    if DriverCommand == 1:
        NUMFLASH = 0
        pause(100)
        light.set_pixel_color(6, 0xffffff)
        keyboard.type("9")
        light.set_pixel_color(7, 0x00ffff)
matrixKeypad.keypad.on_event(6, 0, MatrixKeypadButtonEvent.UP, on_keypad_up9)

def on_keypad_click19():
    global DriverCommand, NUMFLASH
    keyboard.type("t")
    light.set_all(0x000000)
    light.set_pixel_color(31, 0xffffff)
    pause(100)
    keyboard.type("!")
    keyboard.type("dq")
    DriverCommand = 1
    NUMFLASH = 1
matrixKeypad.keypad.on_event(7, 3, MatrixKeypadButtonEvent.CLICK, on_keypad_click19)

def on_keypad_up10():
    global NUMFLASH
    if DriverCommand == 1:
        NUMFLASH = 0
        pause(250)
        light.set_pixel_color(20, 0xffffff)
        keyboard.type("1")
        light.set_pixel_color(7, 0x00ffff)
matrixKeypad.keypad.on_event(4, 2, MatrixKeypadButtonEvent.UP, on_keypad_up10)

def on_keypad_click20():
    global DriverCommand, NUMFLASH
    keyboard.type("t")
    light.set_all(0x000000)
    light.set_pixel_color(30, 0xffffff)
    pause(100)
    keyboard.type("!")
    keyboard.type("black")
    DriverCommand = 1
    NUMFLASH = 1
matrixKeypad.keypad.on_event(6, 3, MatrixKeypadButtonEvent.CLICK, on_keypad_click20)

def numLED():
    pass
QwkRpr = 0
Tire = 0
NUMFLASH = 0
DriverCommand = 0
DriverCommand = 1
NUMFLASH = 1
pause(2000)
DriverCommand = 0
NUMFLASH = 0
pause(2000)
light.set_pixel_color(7, 0x00ffff)

def on_forever():
    if NUMFLASH == 1:
        light.set_pixel_color(20, 0xffff00)
        light.set_pixel_color(12, 0xffff00)
        light.set_pixel_color(4, 0xffff00)
        light.set_pixel_color(21, 0xffff00)
        light.set_pixel_color(13, 0xffff00)
        light.set_pixel_color(5, 0xffff00)
        light.set_pixel_color(22, 0xffff00)
        light.set_pixel_color(14, 0xffff00)
        light.set_pixel_color(6, 0xffff00)
        light.set_pixel_color(15, 0xffff00)
forever(on_forever)
