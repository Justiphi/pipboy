from pypboy import BaseModule
from pypboy.modules.map import local_map
from pypboy.modules.map import world_map
import config

if config.GPIO_AVAILABLE:
    import RPi.GPIO as GPIO

class Module(BaseModule):

    label = "MAP"

    def __init__(self, *args, **kwargs):
        
        self.submodules = [
            local_map.Module(self),
            world_map.Module(self),
        ]
        super(Module, self).__init__(*args, **kwargs)
        
    def handle_resume(self):
        self.pypboy.header.headline = self.label
        self.pypboy.header.title = ["Map"]
        self.active.handle_action("resume")
        
