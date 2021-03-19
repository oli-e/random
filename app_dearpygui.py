from dearpygui.core import *
from dearpygui.simple import *


def func():
    with window("An App"):
        add_text("i'm okay")

set_main_window_size(540, 720)
set_global_font_scale(1.25)
set_theme("Gold") #Cherry
set_style_window_padding(30, 30)




with window("An App", width=520, height=677):
    set_window_pos("An App", 0, 0)

    add_spacing(count=30)

    add_input_text("Input", width=415, default_value="Type something")
    add_spacing(count=15)
    add_button("Check", callback=func)


start_dearpygui()