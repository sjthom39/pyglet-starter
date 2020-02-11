import pyglet # import the library
window = pyglet.window.Window() # create the window

# Create some text
# label = pyglet.text.Label('Hello, world', x = 200, y = 200)

# Create a sprite
img = pyglet.image.load('samuri')
# Start the event loop
@window.event
def on_draw():
    window.clear()
    ball.x += 1
    ball.draw()

pyglet.app.run()
