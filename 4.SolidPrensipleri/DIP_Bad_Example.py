class LightBulb:
    def turn_on(self):
        print("LightBulb: on")

    def turn_off(self):
        print("LightBulb: off")


class PowerSwitch:
    def __init__(self, light_bulb: LightBulb):
        self.light_bulb = light_bulb
        self.on = False

    def press(self):
        if self.on:
            self.light_bulb.turn_off()
        else:
            self.light_bulb.turn_on()
            self.on = True


if __name__ == '__main__':
    light_bulb = LightBulb()
    switch = PowerSwitch(light_bulb)
    switch.press()
    switch.press()
