python3 ~/qtile/scripts/pacman-install-script.py
python3 ~/qtile/scripts/yay-install-script.py
cp -r ~/qtile/config/* ~/.config/
sudo cp ~/qtile/lightdm/lightdm-gtk-greeter.conf /etc/lightdm/
sudo cp ~/.config/wallpapers/mountain1.jpg /usr/share/pixmaps/
sudo cp ~/qtile/touchpad/30-touchpad.conf /etc/X11/xorg.conf.d/
cd ~/qtile/home/
cp -r .moc .oh-my-zsh .scripts ~/
cp .bash_profile .bashrc .p10k.zsh .zshrc ~/
chsh -s $(which zsh)
sudo cp -r ~/qtile/fonts/Iosevka-Mayukai /usr/share/fonts/
sh ~/qtile/scripts/font.sh
sh ~/qtile/scripts/missing.sh
sh ~/qtile/scripts/python_install_pip/python_all.sh
cd ~/.config/suckless-tools/dmenu-5.2/
sudo make clean install
cd ~/.config/suckless-tools/st-0.9/
sudo make clean install
cd ~

