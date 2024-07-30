# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/DanielPerezMoralesDev13
# Email: danielperezdev@proton.me

from typing import Dict, Any
from toml import loads

hardhacker: Dict[str, Any] = loads(s = """\
    # hardhacker colorscheme for alacritty
    # by xin wu, https//github.com/hardhackerlabs/theme-alacritty

    # Default colors
    [colors.primary]
    background = '#282433'
    foreground = '#eee9fc'

    [colors.cursor]
    text = '#eee9fc'
    cursor = '#eee9fc'

    # Normal colors
    [colors.normal]
    black   = '#282433'
    red     = '#e965a5'
    green   = '#b1f2a7'
    yellow  = '#ebde76'
    blue    = '#b1baf4'
    magenta = '#e192ef'
    cyan    = '#b3f4f3'
    white   = '#eee9fc'

    # Bright colors
    [colors.bright]
    black   = '#3f3951'
    red     = '#e965a5'
    green   = '#b1f2a7'
    yellow  = '#ebde76'
    blue    = '#b1baf4'
    magenta = '#e192ef'
    cyan    = '#b3f4f3'
    white   = '#eee9fc'
    """
)