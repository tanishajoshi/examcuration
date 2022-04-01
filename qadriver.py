"""This is the main."""
from view.qaview import handle_view
from controller.qacontroller import setup

if __name__ == "__main__":
    setup()
    handle_view()
