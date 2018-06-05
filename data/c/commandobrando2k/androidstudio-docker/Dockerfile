FROM ubuntu:16.04  
  
RUN echo "deb http://ppa.launchpad.net/ubuntu-desktop/ubuntu-make/ubuntu
xenial main" > \  
/etc/apt/sources.list.d/ubuntu-make-xenial.list && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys A1231595  
RUN apt-get update && \  
apt-get install -y sudo mesa-utils pciutils pulseaudio ubuntu-make  
  
ENV USER=ubuntu UID=1000 SHELL=/bin/bash  
  
RUN useradd -m -u $UID -s $SHELL $USER  
RUN echo "$USER ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers  
  
USER ubuntu  
RUN umake android --accept-license $HOME/android-studio  
  
ENV ANDROID_HOME=/home/$USER/Android/Sdk \  
QT_XKB_CONFIG_ROOT=/usr/share/X11/xkb  
  
ENTRYPOINT ["/bin/sh", "-c", "$HOME/android-studio/bin/studio.sh"]  

