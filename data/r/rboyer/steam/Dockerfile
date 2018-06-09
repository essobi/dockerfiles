FROM ubuntu:trusty  
# FROM ubuntu:precise  
RUN apt-get update -y  
RUN apt-get install -y \  
python \  
curl \  
python-apt \  
xterm \  
xz-utils \  
zenity  
  
# http://wiki.ros.org/docker/Tutorials/GUI  
RUN apt-get install -y x11-apps  
RUN dpkg --add-architecture i386 && apt-get update -y  
RUN apt-get install -y libgl1-mesa-dri:i386 libgl1-mesa-glx:i386 libc6:i386  
# lspci  
RUN apt-get install -y pciutils  
# dbus-launch  
RUN apt-get install -y dbus-x11  
  
# https://github.com/arno01/steam/blob/master/Dockerfile  
RUN apt-get install -y binutils pulseaudio  
  
RUN echo "deb [arch=amd64,i386] http://repo.steampowered.com/steam/ precise
steam" > /etc/apt/sources.list.d/tmp-steam.list && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv
0xF24AEA9FB05498B7 && \  
apt-get update && \  
apt-get install -y steam-launcher  
  
RUN apt-get -fy install  
RUN apt-get -y install binutils pciutils pulseaudio libcanberra-gtk-module \  
libopenal1 libnss3 libgconf-2-4 libxss1 libnm-glib4 \  
libglu1-mesa locales libsdl2-image-2.0 \  
mesa-utils:i386 \  
libstdc++5 libstdc++5:i386 libbz2-1.0:i386 \  
libsdl2-2.0-0 libsdl2-2.0-0:i386 \  
libgl1-mesa-dri:i386 libgl1-mesa-glx:i386 libc6:i386 \  
libxtst6:i386 libxrandr2:i386 libglib2.0-0:i386 \  
libgtk2.0-0:i386 libgdk-pixbuf2.0-0:i386 libsm6:i386 \  
libice6:i386 libopenal1:i386 libdbus-glib-1-2:i386 \  
libusb-1.0-0:i386 \  
libnss3:i386 libgconf-2-4:i386 libxss1:i386 libcurl3:i386 \  
libv8-dev:i386 \  
libcanberra-gtk-module:i386 libpulse0:i386 attr  
  
# COPY steam_latest.deb /tmp/steam.deb  
# RUN dpkg -i /tmp/steam.deb  
RUN apt-get install -y fonts-liberation ttf-ubuntu-font-family  
  
RUN echo "dash dash/sh boolean false" | debconf-set-selections &&
DEBIAN_FRONTEND=noninteractive dpkg-reconfigure dash  
  
RUN locale-gen en_US.UTF-8 && update-locale  
  
RUN adduser --disabled-password --gecos 'Steam' rboyer  
RUN usermod -aG sudo rboyer  
RUN usermod -aG video rboyer  
RUN usermod -aG adm rboyer  
RUN usermod -aG cdrom rboyer  
RUN usermod -aG dip rboyer  
RUN usermod -aG plugdev rboyer  
RUN echo "rboyer ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers.d/rboyer && \  
chmod 0440 /etc/sudoers.d/rboyer  
  
USER rboyer  
CMD ["steam"]  
  
#sh: lspci: command not found  
#libGL error: failed to open drm device: Permission denied  
#libGL error: failed to load driver: i965  

