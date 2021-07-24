matrixKeypad.keypad.onEvent(3, 3, MatrixKeypadButtonEvent.Click, function () {
    keyboard.type("t")
    light.setAll(0x000000)
    light.setPixelColor(27, 0xffffff)
    pause(100)
    keyboard.type("!")
    keyboard.type("clear")
    DriverCommand = 1
    NUMFLASH = 1
})
matrixKeypad.keypad.onEvent(1, 2, MatrixKeypadButtonEvent.Click, function () {
    if (Tire == 0) {
        Tire = 1
        tyre()
    } else {
        Tire = 0
        tyre()
    }
})
matrixKeypad.keypad.onEvent(1, 1, MatrixKeypadButtonEvent.Click, function () {
    keyboard.type("t")
    light.setPixelColor(9, 0xffff00)
    pause(100)
    keyboard.type("Pitting In")
    pause(100)
    enter()
})
matrixKeypad.keypad.onEvent(4, 3, MatrixKeypadButtonEvent.Click, function () {
    keyboard.type("t")
    light.setAll(0x000000)
    light.setPixelColor(28, 0xffffff)
    pause(100)
    keyboard.type("!")
    keyboard.type("waveby")
    DriverCommand = 1
    NUMFLASH = 1
})
matrixKeypad.keypad.onEvent(0, 2, MatrixKeypadButtonEvent.Click, function () {
    if (QwkRpr == 0) {
        QwkRpr = 1
        QwkR()
    } else {
        QwkRpr = 0
        QwkR()
    }
})
matrixKeypad.keypad.onEvent(0, 3, MatrixKeypadButtonEvent.Click, function () {
    keyboard.type("t")
    light.setPixelColor(24, 0xffff00)
    pause(100)
    keyboard.type("!yellow")
    pause(100)
    enter()
})
matrixKeypad.keypad.onEvent(7, 1, MatrixKeypadButtonEvent.Up, function () {
    if (DriverCommand == 1) {
        NUMFLASH = 0
        pause(100)
        light.setPixelColor(15, 0x00ffff)
        keyboard.type("0")
        light.setPixelColor(7, 0xffff00)
    }
})
matrixKeypad.keypad.onEvent(1, 0, MatrixKeypadButtonEvent.Click, function () {
    keyboard.type("t")
    light.setPixelColor(1, 0xffff00)
    pause(100)
    keyboard.type("Pitting Out")
    pause(100)
    enter()
})
matrixKeypad.keypad.onEvent(4, 1, MatrixKeypadButtonEvent.Up, function () {
    if (DriverCommand == 1) {
        NUMFLASH = 0
        pause(100)
        light.setPixelColor(12, 0xffffff)
        keyboard.type("2")
        light.setPixelColor(7, 0x00ffff)
    }
})
matrixKeypad.keypad.onEvent(2, 3, MatrixKeypadButtonEvent.Click, function () {
    keyboard.type("t")
    light.setPixelColor(26, 0xffff00)
    pause(100)
    keyboard.type("!")
    keyboard.type("restart double")
    pause(100)
    enter()
})
matrixKeypad.keypad.onEvent(6, 1, MatrixKeypadButtonEvent.Up, function () {
    if (DriverCommand == 1) {
        NUMFLASH = 0
        pause(100)
        light.setPixelColor(14, 0xffffff)
        keyboard.type("8")
        light.setPixelColor(7, 0x00ffff)
    }
})
matrixKeypad.keypad.onEvent(1, 3, MatrixKeypadButtonEvent.Click, function () {
    keyboard.type("t")
    light.setPixelColor(25, 0xffff00)
    pause(100)
    keyboard.type("!")
    keyboard.type("restart single")
    pause(100)
    enter()
})
matrixKeypad.keypad.onEvent(3, 1, MatrixKeypadButtonEvent.Click, function () {
    keyboard.type("t")
    light.setPixelColor(11, 0xffff00)
    pause(100)
    keyboard.type("!")
    keyboard.type("advance")
    pause(100)
    enter()
})
matrixKeypad.keypad.onEvent(7, 0, MatrixKeypadButtonEvent.Click, function () {
    light.setPixelColor(7, 0xffffff)
    DriverCommand = 0
    NUMFLASH = 0
    enter()
})
matrixKeypad.keypad.onEvent(3, 0, MatrixKeypadButtonEvent.Click, function () {
    keyboard.type("t")
    light.setPixelColor(3, 0xffff00)
    pause(100)
    keyboard.type("!")
    keyboard.type("help")
    pause(100)
    enter()
})
matrixKeypad.keypad.onEvent(5, 2, MatrixKeypadButtonEvent.Up, function () {
    if (DriverCommand == 1) {
        NUMFLASH = 0
        pause(100)
        light.setPixelColor(21, 0xffffff)
        keyboard.type("4")
        light.setPixelColor(7, 0x00ffff)
    }
})
function tyre () {
    if (Tire == 1) {
        light.setPixelColor(17, 0xffff00)
        pause(100)
        keyboard.type("t")
        pause(500)
        keyboard.type("#")
        keyboard.type("lf rf lr rr")
        keyboard.functionKey(KeyboardFunctionKey.Enter, KeyboardKeyEvent.Press)
        keyboard.functionKey(KeyboardFunctionKey.Esc, KeyboardKeyEvent.Press)
    } else {
        light.setPixelColor(17, 0x000000)
        pause(100)
        keyboard.type("t")
        pause(500)
        keyboard.type("#")
        keyboard.type("!cleartires")
        keyboard.functionKey(KeyboardFunctionKey.Enter, KeyboardKeyEvent.Press)
        keyboard.functionKey(KeyboardFunctionKey.Esc, KeyboardKeyEvent.Press)
    }
}
matrixKeypad.keypad.onEvent(0, 0, MatrixKeypadButtonEvent.Click, function () {
    keyboard.type("t")
    light.setPixelColor(0, 0xffff00)
    pause(100)
    keyboard.type("Pass Right")
    pause(100)
    enter()
})
function enter () {
    keyboard.functionKey(KeyboardFunctionKey.Enter, KeyboardKeyEvent.Press)
    pause(100)
    keyboard.functionKey(KeyboardFunctionKey.Esc, KeyboardKeyEvent.Press)
    pause(100)
    light.setAll(0x000000)
    pause(500)
    light.setAll(0xffffff)
}
matrixKeypad.keypad.onEvent(2, 2, MatrixKeypadButtonEvent.Click, function () {
    light.setPixelColor(18, 0xffff00)
    pause(100)
    keyboard.type("t")
    pause(500)
    keyboard.type("#")
    keyboard.type("fuel 2g")
    pause(100)
    enter()
})
matrixKeypad.keypad.onEvent(5, 1, MatrixKeypadButtonEvent.Up, function () {
    if (DriverCommand == 1) {
        NUMFLASH = 0
        pause(100)
        light.setPixelColor(13, 0xffffff)
        keyboard.type("5")
        light.setPixelColor(7, 0x00ffff)
    }
})
matrixKeypad.keypad.onEvent(5, 0, MatrixKeypadButtonEvent.Up, function () {
    if (DriverCommand == 1) {
        NUMFLASH = 0
        pause(100)
        light.setPixelColor(5, 0xffffff)
        keyboard.type("6")
        light.setPixelColor(7, 0x00ffff)
    }
})
matrixKeypad.keypad.onEvent(4, 0, MatrixKeypadButtonEvent.Up, function () {
    if (DriverCommand == 1) {
        NUMFLASH = 0
        pause(100)
        light.setPixelColor(4, 0xffffff)
        keyboard.type("3")
        light.setPixelColor(7, 0x00ffff)
    }
})
matrixKeypad.keypad.onEvent(5, 3, MatrixKeypadButtonEvent.Click, function () {
    keyboard.type("t")
    light.setAll(0x000000)
    light.setPixelColor(29, 0xffffff)
    pause(100)
    keyboard.type("!")
    keyboard.type("eol")
    DriverCommand = 1
    NUMFLASH = 1
})
matrixKeypad.keypad.onEvent(3, 2, MatrixKeypadButtonEvent.Click, function () {
    keyboard.type("t")
    light.setAll(0x000000)
    light.setPixelColor(19, 0xffffff)
    pause(100)
    keyboard.type("!")
    keyboard.type("remove")
    DriverCommand = 1
    NUMFLASH = 1
})
function QwkR () {
    if (QwkRpr == 1) {
        light.setPixelColor(16, 0xffff00)
        pause(100)
        keyboard.type("t")
        pause(500)
        keyboard.type("#")
        keyboard.type("fr")
        keyboard.functionKey(KeyboardFunctionKey.Enter, KeyboardKeyEvent.Press)
        keyboard.functionKey(KeyboardFunctionKey.Esc, KeyboardKeyEvent.Press)
    } else {
        light.setPixelColor(16, 0x000000)
        pause(100)
        keyboard.type("t")
        pause(500)
        keyboard.type("#")
        keyboard.type("!fr")
        keyboard.functionKey(KeyboardFunctionKey.Enter, KeyboardKeyEvent.Press)
        keyboard.functionKey(KeyboardFunctionKey.Esc, KeyboardKeyEvent.Press)
    }
}
matrixKeypad.keypad.onEvent(7, 2, MatrixKeypadButtonEvent.Click, function () {
    light.setPixelColor(23, 0xffffff)
    keyboard.functionKey(KeyboardFunctionKey.Esc, KeyboardKeyEvent.Press)
    DriverCommand = 0
    NUMFLASH = 0
    pause(250)
    light.setAll(0x000000)
    enter()
})
matrixKeypad.keypad.onEvent(0, 1, MatrixKeypadButtonEvent.Click, function () {
    keyboard.type("t")
    light.setPixelColor(8, 0xffff00)
    pause(100)
    keyboard.type("Pass Left")
    pause(100)
    enter()
})
matrixKeypad.keypad.onEvent(6, 2, MatrixKeypadButtonEvent.Up, function () {
    if (DriverCommand == 1) {
        NUMFLASH = 0
        pause(100)
        light.setPixelColor(22, 0xffffff)
        keyboard.type("7")
        light.setPixelColor(7, 0x00ffff)
    }
})
matrixKeypad.keypad.onEvent(6, 0, MatrixKeypadButtonEvent.Up, function () {
    if (DriverCommand == 1) {
        NUMFLASH = 0
        pause(100)
        light.setPixelColor(6, 0xffffff)
        keyboard.type("9")
        light.setPixelColor(7, 0x00ffff)
    }
})
matrixKeypad.keypad.onEvent(7, 3, MatrixKeypadButtonEvent.Click, function () {
    keyboard.type("t")
    light.setAll(0x000000)
    light.setPixelColor(31, 0xffffff)
    pause(100)
    keyboard.type("!")
    keyboard.type("dq")
    DriverCommand = 1
    NUMFLASH = 1
})
matrixKeypad.keypad.onEvent(4, 2, MatrixKeypadButtonEvent.Up, function () {
    if (DriverCommand == 1) {
        NUMFLASH = 0
        pause(250)
        light.setPixelColor(20, 0xffffff)
        keyboard.type("1")
        light.setPixelColor(7, 0x00ffff)
    }
})
matrixKeypad.keypad.onEvent(6, 3, MatrixKeypadButtonEvent.Click, function () {
    keyboard.type("t")
    light.setAll(0x000000)
    light.setPixelColor(30, 0xffffff)
    pause(100)
    keyboard.type("!")
    keyboard.type("black")
    DriverCommand = 1
    NUMFLASH = 1
})
function numLED () {
	
}
let QwkRpr = 0
let Tire = 0
let NUMFLASH = 0
let DriverCommand = 0
DriverCommand = 1
NUMFLASH = 1
pause(2000)
DriverCommand = 0
NUMFLASH = 0
pause(2000)
light.setPixelColor(7, 0x00ffff)
forever(function () {
    if (NUMFLASH == 1) {
        light.setPixelColor(20, 0xffff00)
        light.setPixelColor(12, 0xffff00)
        light.setPixelColor(4, 0xffff00)
        light.setPixelColor(21, 0xffff00)
        light.setPixelColor(13, 0xffff00)
        light.setPixelColor(5, 0xffff00)
        light.setPixelColor(22, 0xffff00)
        light.setPixelColor(14, 0xffff00)
        light.setPixelColor(6, 0xffff00)
        light.setPixelColor(15, 0xffff00)
    }
})
