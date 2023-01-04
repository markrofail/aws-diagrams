from pathlib import Path

from diagrams.custom import Custom


def create_icon(filename):
    class CustomIcon(Custom):
        _icon = Path(__file__).parent / filename

    return CustomIcon
