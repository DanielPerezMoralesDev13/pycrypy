# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/DanielPerezMoralesDev13
# Email: danielperezdev@proton.me

from typing import Dict, Any
from toml import loads

argonaut: Dict[str, Any] = loads(s = """\
    # Default colors
    [colors.primary]
    background = '#292C3E'
    foreground = '#EBEBEB'

    # Cursor colors
    [colors.cursor]
    text = '#EBEBEB'
    cursor = '#FF261E'

    # Normal colors
    [colors.normal]
    black   = '#0d0d0d'
    red     = '#FF301B'
    green   = '#A0E521'
    yellow  = '#FFC620'
    blue    = '#1BA6FA'
    magenta = '#8763B8'
    cyan    = '#21DEEF'
    white   = '#EBEBEB'

    # Bright colors
    [colors.bright]
    black   = '#6D7070'
    red     = '#FF4352'
    green   = '#B8E466'
    yellow  = '#FFD750'
    blue    = '#1BA6FA'
    magenta = '#A578EA'
    cyan    = '#73FBF1'
    white   = '#FEFEF8'
    """
)