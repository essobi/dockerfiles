FROM base/devel  
LABEL maintainer="tralamazza"  
  
ENV XTENSA_TOOLCHAIN xtensa-esp32-elf-linux64-1.22.0-80-g6c4433a-5.2.0  
# init + base packages  
RUN rm -rf /etc/pacman.d/gnupg && \  
pacman-key --init && \  
pacman-key --populate archlinux && \  
pacman-key --refresh-keys --keyserver ipv4.pool.sks-keyservers.net && \  
pacman -Suy --noconfirm wget python git zip  
  
# the yak: aur packages -> pacaur -> cower -> import gpg keys -> makepkg can't
root -> create makepkg user  
RUN useradd -m --shell=/bin/false build && \  
passwd -d build && \  
echo "build ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers && \  
sudo -u build sh -c 'gpg --keyserver ipv4.pool.sks-keyservers.net --recv-keys
1EB2638FF56C0C53' && \  
sudo -u build sh -c 'cd ~ && git clone https://aur.archlinux.org/cower.git &&
cd cower && makepkg -si --noconfirm' && \  
sudo -u build sh -c 'cd ~ && git clone https://aur.archlinux.org/pacaur.git &&
cd pacaur && makepkg -si --noconfirm'  
# now we can use `sudo -u build sh -c 'pacaur -S ...'` to install AUR packages  
# ARM + Segger tools  
RUN pacman -S --noconfirm arm-none-eabi-binutils arm-none-eabi-gcc arm-none-
eabi-gdb arm-none-eabi-newlib && \  
sudo -u build sh -c 'pacaur -S --noconfirm jlink-software-and-documentation'  
# AVR  
RUN pacman -S --noconfirm avr-binutils avr-gcc avr-gdb avr-libc avrdude  
  
# Xtensa (https://esp-idf.readthedocs.io/en/latest/get-started/linux-
setup.html)  
RUN sudo -u build sh -c 'gpg --keyserver ipv4.pool.sks-keyservers.net --recv-
keys 702353E0F7E48EDB' && \  
sudo -u build sh -c 'pacaur -S --noconfirm ncurses5-compat-libs gcc-xtensa-
esp32-elf-bin' && \  
pacman -S --noconfirm gperf python2-pyserial && \  
mkdir -p xtensa && \  
cd xtensa && \  
wget https://dl.espressif.com/dl/${XTENSA_TOOLCHAIN}.tar.gz && \  
tar xf ${XTENSA_TOOLCHAIN}.tar.gz && \  
rm ${XTENSA_TOOLCHAIN}.tar.gz  
  
# Java  
RUN pacman -S --noconfirm jre9-openjdk  
  
# Cache clean  
RUN sudo pacman -Sc  

