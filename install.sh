python3 ~/laptop/scripts/pacman-install-script.py
python3 ~/laptop/scripts/yay-install-script.py
cp -r ~/laptop/config/* ~/.config/
sudo cp ~/laptop/lightdm/lightdm-gtk-greeter.conf /etc/lightdm/
sudo cp ~/.config/wallpapers/mountain1.jpg /usr/share/pixmaps/
sudo cp ~/laptop/touchpad/30-touchpad.conf /etc/X11/xorg.conf.d/
cd ~/laptop/home/
cp -r .moc .oh-my-zsh .scripts
cp .bash_profile .bashrc .p10k.zsh .zshrc
chsh -s $(which zsh)
sudo cp -r ~/laptop/fonts/Iosevka-Mayukai /usr/share/fonts/
sh ~/laptop/scripts/font.sh
sh ~/laptop/scripts/missing.sh
sh ~/laptop/scripts/python_install_pip/python_all.sh
