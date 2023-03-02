from time import sleep
import os

print("INSTALLING SOFTWARE FROM AUR!")
sleep(5)

programs = [
        'mkinitcpio-firmware',
	    'linux-firmware-qlogic',
	    'upd72020x-fw',
	    'faac',
	    'wd719x-firmware',
	    'aic94xx-firmware',
	    'qed-git',
	    'dracula-gtk-theme',
	    'flashplugin',
	    'dracula-cursors-git',
	    'whatsapp-nativefier',
	    'telegram-desktop',
	    'viber',
	    'deadbeef',
	    'megatools',
	    'spotify',
	    'spotifywm-git',
	    'ttf-comic-mono-git',
	    'picom-git',
	    'powrline-fonts',
	    'termite',
	    'brave-bin',
	    'ttf-consolas-ligaturized',
	    'ttf-material-design-icons',
	    'alacritty-themes',
	    'nordic-theme-git',
	    'moc-pulse',
	    'mocicon',
	    'betterlockscreen',
	    'papirus-folders-nordic',
	    'nordic-wallpapers',
	    'catppuccin-gtk-theme-mocha',
	    'papirus-folders-catppuccin-git',
	    'catppuccin-cursors-mocha',
	    'caffeine-ng',
        'python-django-docs',
        ]

for program in programs:
    try:
        os.system('yay -S --noconfirm' + ' ' + program)
        print(program + ' ' + 'installed successfully!')
    except:
        exit(program + ' ' + 'failed to install!')

print('Programs successfully installed!')
sleep(5)
exit()
