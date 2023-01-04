from diagrams import Diagram as _Diagram

TOP_BOTTOM = "TB"
BOTTOM_TOP = "BT"
LEFT_RIGHT = "LR"
RIGHT_LEFT = "RL"


class Diagram(_Diagram):
    def __init__(self, *args, dark_mode=False, direction=LEFT_RIGHT, **kwargs):
        font_color = "white" if dark_mode else "black"
        node_attr = {
            "fontcolor": font_color,
        }

        graph_attr = {
            "bgcolor": "transparent",
            "fontcolor": font_color,
            "penwidth": "2",
        }

        super().__init__(*args, show=False, graph_attr=graph_attr, node_attr=node_attr, direction=direction, **kwargs)
