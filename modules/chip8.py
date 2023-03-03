from modules.renderer import Renderer
from modules.keyboard import Keyboard

def play():
    print("play")
    keyboard = Keyboard()
    display = Renderer(14)
    display.run(keyboard)

    memory = int[4096]

def translate_op_code(opcode):
    pass
    
