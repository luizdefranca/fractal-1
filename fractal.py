import turtle as trtl
def fractal(length = 100):
        if length < 10:
                return

        trtl.fd(length)
        fractal(length * 0.3)
        trtl.left(144)
        trtl.fd(length)
        fractal(length * 0.3)
        trtl.left(144)
        trtl.fd(length)
        fractal(length * 0.3)
        trtl.left(144)
        trtl.fd(length)
        fractal(length * 0.3)
        trtl.left(144)
        trtl.fd(length)
        fractal(length * 0.3)
        trtl.left(144)
        return
