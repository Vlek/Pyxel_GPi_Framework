import pyxel


class Framework:
    def __init__(self) -> None:
        pyxel.init(255, 239)

    # Maybe I should dunder these so that someone doesn't overwrite them?
    def update(self) -> None:
        """
        The update function that will be given to Pyxel at the end. This is
        going to encompass a lot of stuff for us, including the button handlers.

        Anything that operates on ticks will also likely live here.
        """

        """
        TODO: Handle button presses here!
         This will likely be its own separate class. The whole reason behind
         this is to create the sanest way to handle all of the different button
         press event types, including button down, up, and pressed events.

        TODO: Consider handler functions
         In order to do this, we may want to be able to register handler
         functions for the button presses that will be called if the button
         enters a predefined state (or states).
        """
        pass

    def draw(self) -> None:
        """
        The draw function that will be given to Pyxel. This will have to include
        the ability to add and remove functions to a queue for handling drawing
        multiple layers on top of each other, like with game maps and gui
        overlays.
        """

        """
        TODO: Add logic for handling multiple draw functions
        """
        pass

    def run(self) -> None:
        pyxel.run(self.update, self.draw)
