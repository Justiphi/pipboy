from pypboy import BaseModule
from pypboy.modules.stats import status
from pypboy.modules.stats import special
from pypboy.modules.stats import skills
from pypboy.modules.stats import perks
import config

if config.GPIO_AVAILABLE:
    import RPi.GPIO as GPIO

class Module(BaseModule):

    label = "STATS"

    def __init__(self, *args, **kwargs):

        self.submodules = [
            status.Module(self),
            special.Module(self),
            skills.Module(self),
            perks.Module(self)
        ]
        super(Module, self).__init__(*args, **kwargs)
        
    def handle_resume(self):

        self.pypboy.header.headline = self.label
        self.pypboy.header.title = ["AP  75/140","HP  526/757", "LVL108"]
        self.active.handle_action("resume")
