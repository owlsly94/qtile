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
    
    # Workspace icons: 
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
    
    # Front arrow:
    right_arrow(catppuccin['green'], catppuccin['bg']),
    
    # Current Layout name:
    CurrentLayout(
        background=catppuccin['green'],
        foreground=catppuccin['bg'],
        margin=10,
        ),

    # Back arrow:
    right_arrow(catppuccin['bg'], catppuccin['green']),

    # Running program name:
    WindowName(
        background=catppuccin['bg'],
        foreground=catppuccin['fg'],
        font='Comic Mono',
        fontsize='13'
        ),

    # Front arrow:
    right_arrow(catppuccin['mauve'], catppuccin['bg']),
    
    # CPU Usage:
    CPU(
        format='󰘚 {load_percent}%',
        background=catppuccin['mauve'],
        foreground=catppuccin['bg']
        ),
    
    # Back arrow:
    right_arrow(catppuccin['blue'], catppuccin['mauve']),

    # CPU Temperature:
    ThermalZone(
        format=' {temp}°C',
        background=catppuccin['blue'],
        high=70,
        crit=80,
        fgcolor_crit=catppuccin['red'],
        fgcolor_high=catppuccin['yellow'],
        fgcolor_normal=catppuccin['bg'],
        zone='/sys/class/thermal/thermal_zone0/temp',
        update_interval=2,
        ),

    # Front arrow:
    right_arrow(catppuccin['green'], catppuccin['blue']),
    
    # RAM Memory:
    Memory(
        format=' {MemUsed: .0f}{mm}',
        measure_mem='M',
        background=catppuccin['green'],
        foreground=catppuccin['bg'],
        ),

    # Back arrow:
    right_arrow(catppuccin['yellow'], catppuccin['green']),

    # Volume with Pulse Audio:
    PulseVolume(
        fmt='󰓃 {:>4}',
        #emoji=True,
        background=catppuccin['yellow'],
        foreground=catppuccin['bg'],
        update_interval=0.1,
        ),

    # Front arrow:
    right_arrow(catppuccin['peach'], catppuccin['yellow']),

    # Date:
    Clock(
        format=' %a%e-%b',
        background=catppuccin['peach'],
        foreground=catppuccin['bg'],
        ),

    # Back arrow:
    right_arrow(catppuccin['red'], catppuccin['peach']),

    # Clock:
    Clock(
        format=' %H:%M',
        background=catppuccin['red'],
        foreground=catppuccin['bg'],
        ),

    # Front arrow
    right_arrow(catppuccin['bg'], catppuccin['red']),

    Systray(
        background=catppuccin['bg'],
        iconsize=30,
        ),

    ],
          size=BAR_HEIGHT,
          margin=0,
)
