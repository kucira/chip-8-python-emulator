class Keyboard:
    def __init__(self) -> None:
        self.KEYMAP = {
            49: 0x1, #1
            50: 0x2,
            51: 0x3,
            52: 0xc,
            81: 0x4,
            87: 0x5,
            69: 0x6,
            82: 0xD,
            65: 0x7,
            83: 0x8,
            68: 0x9,
            70: 0xE,
            90: 0xA,
            88: 0x0,
            67: 0xB,
            86: 0xF,
        }

        self.keyPressed = []
        self.onNextKeyPress = None

    def keyDown(self, keyCode):
        print('keydown', keyCode)
        key = self.KEYMAP[keyCode]
        self.keyPressed[key] = True

        if(self.onNextKeyPress != None and key):
            self.onNextKeyPress(int(key))
            self.onNextKeyPress = None

    def keyUp(self,keyCode):
        print('keyup', keyCode)
        key = self.KEYMAP[keyCode]
        self.keyPressed[key] = False
