from pypboy import BaseModule
from pypboy.modules.radio import radio
import config

if config.GPIO_AVAILABLE:
    import RPi.GPIO as GPIO

class Module(BaseModule):

    label = "RADIO"
    GPIO_LED_ID = 24

    def __init__(self, *args, **kwargs):
        
        self.submodules = [
            radio.Module(self)
        ]
        super(Module, self).__init__(*args, **kwargs)
        
    def handle_resume(self):
        self.pypboy.header.headline = self.label
        self.pypboy.header.title = ["Radio"]
        self.active.handle_action("resume")
        
