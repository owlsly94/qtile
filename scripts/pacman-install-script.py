from time import sleep
import os

print("INSTALLING SOFTWARE FROM PACMAN MANAGER!")
sleep(5)

programs = [
        'lxappearance',
        'pcmanfm',
        'htop',
        'nomacs',
        'pavucontrol',
        'pamixer',
        'alsa-firmware',
        'alsa-utils',
        'alsa-plugins',
        'pulseaudio-alsa',
        'flameshot',
        'ttf-jetbrains-mono',
        'zsh',
        'rofi',
        'picom',
        'feh',
        'w3m',
        'man',
        'rsync',
        'rclone',
        'firefox',
        'mpv',
        'vlc',
        'qt5ct',
        'libreoffice-still',
        'libreoffice-still-sr-latin',
        'lightdm',
        'lightdm-gtk-greeter',
        'curl',
        'gtop',
        'neofetch',
        'unrar',
        'unzip',
        'zip',
        'wget',
        'zenity',
        'zsh-completions',
        'code',
        'exfat-utils',
        'apache',
        'clang',
        'cmake',
        'electron',
        'git',
        'gcc',
        'glibc',
        'nodejs',
        'php',
        'php-apache',
        'yarn',
        'chromium',
        'polkit-gnome',
        'nodejs-material-design-icons',
        'gnome-keyring',
        'ranger',
        'xfce4-power-manager',
        'networkmanager',
        'network-manager-applet',
        'neovim',
        'jre-openjdk',
        'jdk-openjdk',
        ]
for program in programs:
    try:
        os.system('sudo pacman -S --noconfirm' + ' ' + program)
        print(program + ' ' + "installed successfully!")
    except:
        exit(program + ' ' + "failed to install!")

print("Programs successfully installed!")
sleep(5)
exit()
