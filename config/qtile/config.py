
# Imports:

import os
import subprocess

from libqtile import hook

from libqtile.layout.max import Max
from libqtile.layout.xmonad import MonadTall
from libqtile.layout.columns import Columns
from libqtile.layout.floating import Floating

from libqtile.config import Click, Drag, Group, Key, Match, Screen, ScratchPad, DropDown
from libqtile.lazy import lazy

from colors import catppuccin
from bar import bar

# Autostart Hook

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])

# Variables:

mod             = "mod1" # Default Mod Key
sup             = "mod4" # Default Super Key
myFont          = "Iosevka Nerd Font" # Default Font
myTitleFont     = "Iosevka Nerd Font" # Title Font
myTerminal      = "alacritty" # Default Terminal
myBrowser       = "firefox" # Default Browser
myFileManager   = "pcmanfm" # Default File Manager
myEditor        = "code" # Default Editor
myMusicPlayer   = "alacritty -e mocp" # Default Music Player
programLauncher = ["dmenu_run", "-fn", myTitleFont, "-nb", "#1f1d2e", "-nf", "#89b4fa", "-sb", "#89b4fa", "-sf", "#1f1d2e"] # Run DMenu
volumeUp        = "pamixer -i 5" # Volume Up
volumeDown      = "pamixer -d 5" # Volume Down
volumeMute      = "pamixer --mute" # Mute
volumeUnmute    = "pamixer --unmute" # Unmute
rofiLauncher    = "rofi -show drun -show-icons" # Rofi Launcher
powerMenu       = "rofi -show session-menu -modi session-menu:~/.scripts/rofi-power-menu --choices=shutdown/reboot/logout/lockscreen" # Power Menu
wall_changer    = os.path.expanduser("~/.scripts/feh-randomize.sh")

keys = [
    
    # My custom keys:
    
    Key([mod], "Return", lazy.spawn(myTerminal), desc="Launch terminal"),
    Key([sup], "f", lazy.spawn(myBrowser), desc="Open up the default browser"),
    Key([sup, "shift"], "f", lazy.spawn("firefox -p"), desc="Launch Firefox Profiles"),
    Key([mod], "d", lazy.spawn(myFileManager), desc="Open the default file manager"),
    Key([sup], "c", lazy.spawn(myEditor), desc="Launch VS Code"),
    Key([sup], "m", lazy.spawn(myMusicPlayer), desc="Launch Music Player"),
    Key([mod], "p", lazy.spawn(programLauncher), desc="Launch Dmenu"),
    Key([sup], "p", lazy.spawn(rofiLauncher), desc="Launch Rofi launcher!"),
    Key([sup], "r", lazy.spawn(powerMenu), desc="Launch Power Menu!"),
    Key([sup], "w", lazy.spawn(wall_changer, shell=True), desc="Wallpaper changer!"),

    # Sound Keys:

    Key([mod], "F12", lazy.spawn(volumeUp), desc="Volume up!"),
    Key([mod], "F11", lazy.spawn(volumeDown), desc="Volume Down!"),
    Key([mod], "F10", lazy.spawn(volumeMute), desc="Mute!"),
    Key([mod], "F9", lazy.spawn(volumeUnmute),desc="Unmute!"),

    # Qtile Kill Window, Restart and Shutdown Keys:
    
    Key([mod, "shift"], "c", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "shift"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

    # Switch between windows
    
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.

    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),
    
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    
    Key([mod, "control"], "Left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "Right", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "Down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "Up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),
    
    # Toggle between different layouts as defined below
    
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
]

# Groups:
    
groups = [
        Group('1', label="", layout='monadtall'),
        Group('2', label="", layout='monadtall', matches=[Match(wm_class=["firefox"])]),
        Group('3', label="", layout='monadtall', matches=[Match(wm_class=["code-oss"])]),
        Group('4', label="", layout='monadtall', matches=[Match(wm_class=["Pcmanfm"])]),
        Group('5', label="", layout='monadtall', matches=[Match(wm_class=["libreoffice-writer"])]),
        Group('6', label="", layout='monadtall', matches=[Match(wm_class=["whatsapp-nativefier-d40211"])]),
        Group('7', label="", layout='max', matches=[Match(wm_class=["mpv"])]),
        Group('8', label="", layout='monadTall', matches=[Match(wm_class=["Deadbeef"])]),
        Group('9', label="", layout='monadTall', matches=[Match(wm_class=["qBittorrent"])]),
        Group('0', label="󰭹", layout='monadTall', matches=[Match(wm_class=["ViberPC"])])
        ]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            desc="move focused window to group {}".format(i.name)),
        ])

# ScartchPads

groups.append(ScratchPad('scratchpad', [
    DropDown('term', 'alacritty',           width=0.5, height=0.5, x=0.2, y=0.2, opacity=1),
    DropDown('mocp', 'alacritty -e mocp',   width=0.5, height=0.5, x=0.2, y=0.2, opacity=1),
    DropDown('paco', 'pavucontrol',  width=0.4, height=0.6, x=0.3, y=0.1, opacity=1),
    DropDown('rang', 'alacritty -e ranger', width=0.5, height=0.5, x=0.2, y=0.2, opacity=1),
    ]))

keys.extend([
    Key(["control"], "1", lazy.group['scratchpad'].dropdown_toggle('term')),
    Key(["control"], "2", lazy.group['scratchpad'].dropdown_toggle('mocp')),
    Key(["control"], "3", lazy.group['scratchpad'].dropdown_toggle('paco')),
    Key(["control"], "4", lazy.group['scratchpad'].dropdown_toggle('rang')),
])

# Layouts:
    
layouts = [
    MonadTall(
        border_focus='#a6e3a1',
        border_normal='#45475a',
        border_on_single=False,
        border_width=2,
        margin=10,
        ),
    Columns(
        border_focus='#a6e3a1',
        border_normal='#45475a',
        border_width=2,
        margin=10,
        ),
    Max(),

    Floating(
     float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)

]
# Drag floating layouts.

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

widget_defaults = dict(
    font=myFont,
    fontsize=13,
    padding=10,
    background=catppuccin['bg'],
)

extension_defaults = widget_defaults.copy()

# Bar:

screens = [
    Screen(top=bar)
]

# Defaluts:

dgroups_key_binder = None # Turn off, if using simple keys
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = ''
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wmname = "Qtile"
