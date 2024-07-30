# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/DanielPerezMoralesDev13
# Email: danielperezdev@proton.me

from typing import Dict, Any
from toml import loads

gruvbox_material_medium_dark: Dict[str, Any] = loads(s = """\
    # Colors (Gruvbox Material Medium Dark)

    # Default colors
    [colors.primary]
    background = '#282828'
    foreground = '#d4be98'

    # Normal colors
    [colors.normal]
    black   = '#3c3836'
    red     = '#ea6962'
    green   = '#a9b665'
    yellow  = '#d8a657'
    blue    = '#7daea3'
    magenta = '#d3869b'
    cyan    = '#89b482'
    white   = '#d4be98'

    # Bright colors (same as normal colors)
    [colors.bright]
    black   = '#3c3836'
    red     = '#ea6962'
    green   = '#a9b665'
    yellow  = '#d8a657'
    blue    = '#7daea3'
    magenta = '#d3869b'
    cyan    = '#89b482'
    white   = '#d4be98'
    """
)