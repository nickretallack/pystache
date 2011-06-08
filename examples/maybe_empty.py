import pystache

class MaybeEmpty(pystache.View):
    template_path = 'examples'

    def __init__(self, things):
        self.things = things

    def things(self):
        return things
