from pypboy import BaseModule
from pypboy.modules.data import quests
import config

if config.GPIO_AVAILABLE:
    import RPi.GPIO as GPIO

class Module(BaseModule):

    label = "DATA"

    def __init__(self, *args, **kwargs):
        
        self.submodules = [
            quests.Module(self)
        ]
        super(Module, self).__init__(*args, **kwargs)
        
    def handle_resume(self):
        self.pypboy.header.headline = self.label
        self.pypboy.header.title = ["Armageddon"]
        self.active.handle_action("resume")
        
