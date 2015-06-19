class GameSettings(object):
    per_row = 8

    def __init__(self, *args, **kwargs):
        # override any settings if needed
        if kwargs:
            for k, v in kwargs.get('items'):
                setattr(self, k, v)
