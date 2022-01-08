class TV:
    def __init__(self):
        self.is_on = False
        
    def turn_on(self):
        self.is_on = True
    
    def turn_off(self):
        self.is_on = False
    
    def show_status(self):
        on_text = "on" if self.is_on else "off"
        print(f"TV is {on_text}")

tv = TV()
tv.show_status()
tv.turn_on()
tv.show_status()
tv.turn_off()
tv.show_status()
