# Imports from Core

from libqtile.bar import Bar
from libqtile.widget.clock import Clock
from libqtile.widget.cpu import CPU
from libqtile.widget.currentlayout import CurrentLayout
from libqtile.widget.groupbox import GroupBox
from libqtile.widget.memory import Memory
from libqtile.widget.systray import Systray
from libqtile.widget.windowname import WindowName
from libqtile.widget.thermal_zone import ThermalZone
from libqtile.widget.pulse_volume import PulseVolume

# Imports from Customs

from bar_decorations import left_half_circle, right_half_circle, left_arrow, right_arrow, lower_left_triangle
from colors import catppuccin

BAR_HEIGHT = 24

bar = Bar([
    
    GroupBox(
        disable_drag=True,
        active=catppuccin['mauve'],
        inactive=catppuccin['inactive'],
        highlight_method='text',
        background=catppuccin['bg'],
        spacing=5,
        foreground=catppuccin['inactive'],
        padding=3,
        this_current_screen_border=catppuccin['green'],
        ),
    
    right_arrow(catppuccin['green'], catppuccin['bg']),
    
    CurrentLayout(
        background=catppuccin['green'],
        foreground=catppuccin['bg'],
        margin=10,
        ),
    right_arrow(catppuccin['bg'], catppuccin['green']),

    WindowName(
        background=catppuccin['bg'],
        foreground=catppuccin['fg'],
        font='Comic Mono',
        fontsize='13'
        ),
    
    right_arrow(catppuccin['pink'], catppuccin['bg']),
    CPU(
        format='󰘚 {load_percent}%',
        background=catppuccin['pink'],
        foreground=catppuccin['bg']
        ),
    right_arrow(catppuccin['red'], catppuccin['pink']),

    ThermalZone(
        format=' {temp}°C',
        background=catppuccin['red'],
        high=70,
        crit=80,
        fgcolor_crit=catppuccin['blue'],
        fgcolor_high=catppuccin['yellow'],
        fgcolor_normal=catppuccin['bg'],
        zone='/sys/class/thermal/thermal_zone0/temp',
        update_interval=2,
        ),
    right_arrow(catppuccin['peach'], catppuccin['red']),
    
    Memory(
        format=' {MemUsed: .0f}{mm}',
        measure_mem='M',
        background=catppuccin['peach'],
        foreground=catppuccin['bg'],
        ),
    right_arrow(catppuccin['mauve'], catppuccin['peach']),

    PulseVolume(
        fmt='󰓃 {:>4}',
        #emoji=True,
        background=catppuccin['mauve'],
        foreground=catppuccin['bg'],
        update_interval=0.1,
        ),
    right_arrow(catppuccin['blue'], catppuccin['mauve']),

    Clock(
        format='󰃰 %d/%m %A %H:%M',
        background=catppuccin['blue'],
        foreground=catppuccin['bg'],
        ),
    right_arrow(catppuccin['bg'], catppuccin['blue']),
    Systray(
        background=catppuccin['bg'],
        iconsize=30,
        ),

    ],
          size=BAR_HEIGHT,
          margin=0,
)
