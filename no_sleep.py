from pynput import keyboard
from pynput.mouse import Controller


mouse = Controller()

print('press ESC for exit')

while True:
    mouse.position = (10, 20)

    # Перемещение мыши
    mouse.move(5, -5)
    mouse.move(50, 100)

    with keyboard.Events() as events:
    	event = events.get(1.0)
    	if event is None:
    		pass
    	elif event.key == keyboard.Key.esc:
    		break
   