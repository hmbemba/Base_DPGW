from gui.DPGW.BaseView import BaseView
from dataclasses import dataclass
from gui.DPGW.BaseView import BaseView
from gui.DPGW.Container import Container
import dearpygui.dearpygui as dpg


@dataclass
class MyView(BaseView):
    def __post_init__(self):
        self.id = self.getId()
        with dpg.stage(tag=f"Stage_{self.id}"):
            self.top = Container(
                **{
                    "tag": f"top_{self.id}",
                    "show": True,
                    "w": -1,  # -1 is full, 0 is default, .001 to 1 is multiplied to screenWidth, 1.001+ = pixel values
                    "h": -1,  # -1 is full, 0 is default, .001 to 1 is multiplied to screenHeight, 1.001+ = pixel values
                    "autoSizeX": False,  # Overtakes w
                    "autoSizeY": False,  # Overtakes h
                    "itemOrientation": "col",  # row = items stacked left to right, col = items stacked top to btm
                    "horzGap": 0,  # space between items when itemOrientation is row
                    "verticalItemSpacing": [0, 0],
                    "border": True,
                    "borderRadius": 0,
                    "borderColor": [255, 0, 0, 255],  # "orange",
                    "bkgColor": [0, 0, 255, 255],
                    "padding": [0, 0],  # [LR,TB] !Can also be negative
                    "onHover": None,
                    "noScrollBar": True,
                    "font": None,  # "main_20"
                }
            ).create()