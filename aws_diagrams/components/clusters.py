from typing import Optional

from diagrams import Cluster as _Cluster
from diagrams import Node
from diagrams.aws import network

from ..resources import create_icon


class Cluster(_Cluster):
    icon: Optional[Node] = None
    icon_size: int = 25
    default_border_color: str = "#AEB6BE"  # https://graphviz.org/doc/info/colors.html

    def __init__(self, label: str, *args, color: str = None, **kwargs):
        color = color or self.default_border_color
        graph_attr = {
            "bgcolor": "transparent",
            "style": "filled",
            "pencolor": color,
            "fontcolor": "black",
            "margin": "50",
        }

        if self.icon:
            icon_src = self.icon._load_icon(self.icon)
            label = f"""
            <table border="0" bgcolor="{color}">
                <tr>
                    <td fixedsize="true" width="{self.icon_size}" height="{self.icon_size}">
                        <img src="{icon_src}"></img>
                    </td>
                    <td>{label} </td>
                </tr>
            </table>
            """
            label = f"<{label}>".strip().replace("  ", "")

        super().__init__(*args, label=label, graph_attr=graph_attr, **kwargs)


class AvailabilityZone(Cluster):
    default_border_color = "green3"


class VPC(Cluster):
    icon = create_icon("private.png")
    default_border_color = "dodgerblue2"  # https://graphviz.org/doc/info/colors.html


class Account(Cluster):
    icon = create_icon("cloud.png")
    icon_color = "blue"
    default_border_color = "green3"  # https://graphviz.org/doc/info/colors.html


class PrivateSubnet(Cluster):
    icon = network.Privatelink
    default_border_color = "greenyellow"  # https://graphviz.org/doc/info/colors.html


class PublicSubnet(Cluster):
    icon = network.PublicSubnet
    default_border_color = "deepskyblue1"  # https://graphviz.org/doc/info/colors.html
