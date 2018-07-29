class Rect:
    def __init__(self, x, y, w, h):
        self.x = x; self.y = y
        self.w = w; self.h = h

    def __repr__(self):
        return 'x: {}, y: {}, w: {}, h: {}'.format(self.x, self.y, self.w, self.h)
