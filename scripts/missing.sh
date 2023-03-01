#!/bin/bash
###################################################################
##                 _ _   _                  _  _            _    ##
## /\   /\___  ___(_) |_(_)_ __   __ _  ___(_)(_) ___ _ __ | |_  ##
## \ \ / / _ \/ __| | __| | '_ \ / _` |/ __| || |/ _ \ '_ \| __| ##
##  \ V /  __/ (__| | |_| | |_) | (_| | (__| || |  __/ | | | |_  ##
##   \_/ \___|\___|_|\__|_| .__/ \__,_|\___|_|/ |\___|_| |_|\__| ##
##                        |_|               |__/                 ##
###################################################################

# Installing missed apps:
echo "INSTALLING APPS THAT WERE MISSED BY THE BASE INSTALLATION"
sleep 3s
yay -S networkmanager network-manager-applet git vim dialog wpa_supplicant mtools dosfstools base-devel linux-headers pacman-contrib avahi xdg-user-dirs gvfs gvfs-smb nfs-utils inetutils dnsutils bluez bluez-utils alsa-utils pulseaudio linux-firmware mesa mesa-utils alsa-plugins pulseaudio-alsa exfat-utils fuse-common fuse2 fuse3 confuse fuseiso sshfs bash-completion openssh rsync reflector acpi acpi_call tlp dnsmasq openbsd-netcat ipset firewalld sof-firmware nss-mdns acpid os-prober ntfs-3g terminus-font php php-cgi php-gd php-pgsql php-apache --noconfirm

# Installing proper drivers
echo "Installing GPU drivers!"
sleep 3s
sudo pacman -S --noconfirm xf86-video-ati
#sudo pacman -S xf86-input-libinput
#sudo pacman -S --noconfirm xf86-video-amdgpu
#sudo pacman -S --noconfirm xf86-video-intel libva-intel-driver
#sudo pacman -S --noconfirm nvidia nvidia-utils nvidia-settings
#sudo pacman -S --noconfirm vulkan-intel

echo "Installing CPU drivers"
#sudo pacman -S --noconfirm amd-ucode
sudo pacman -S --noconfirm intel-ucode

# Enabling system services for SystemD:
echo "SystemD services enabling..."
sleep 3s

sudo systemctl enable NetworkManager
sudo systemctl enable sshd
sudo systemctl enable httpd
sudo systemctl enable avahi-daemon
sudo systemctl enable tlp # You can disable this if you're not on a laptop, because this is battery tool
sudo systemctl enable reflector.timer
sudo systemctl enable fstrim.timer
sudo systemctl enable firewalld
sudo systemctl enable acpid

echo "SystemD services enabled"
sleep 3s
exit
