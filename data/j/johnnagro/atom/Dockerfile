FROM ubuntu:16.04  
MAINTAINER John Nagro <john.nagro@gmail.com>  
  
RUN apt-get clean && apt-get update  
  
# NOTE: from dpkg --info atom-amd64.deb  
RUN apt-get install -y \  
git \  
gconf2 \  
gconf-service \  
libudev1 \  
libgcrypt20 \  
libnotify4 \  
libxtst6 \  
libnss3 \  
python \  
gvfs-bin \  
xdg-utils \  
libcap2 \  
libgnome-keyring0 \  
gir1.2-gnomekeyring-1.0 \  
lsb-release  
  
# NOTE: extras  
RUN apt-get install -y \  
libgl1-mesa-dri \  
libgl1-mesa-glx \  
libasound2 \  
libxss1 \  
libnss3 \  
libxkbfile1 \  
unity-gtk-module-common \  
dbus-x11 \  
libcanberra-gtk-module  
  
RUN rm -rf /var/lib/apt/lists/*  
  
ENV ATOM_VERSION 1.15.0  
  
ADD https://github.com/atom/atom/releases/download/v${ATOM_VERSION}/atom-
amd64.deb /tmp/atom-amd64.deb  
  
RUN dpkg -i /tmp/atom-amd64.deb  
  
# Autorun atom  
ENTRYPOINT [ "atom", "--foreground" ]  

