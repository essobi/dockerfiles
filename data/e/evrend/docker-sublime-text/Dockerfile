FROM ubuntu:trusty  
MAINTAINER Evren Doğan (evrend@outlook.com)  
  
# For Error ---> cannot create regular file
'/usr/share/icons/hicolor/16x16/apps/' No such file or directory  
RUN mkdir -p /usr/share/icons/hicolor/16x16/apps/  
RUN mkdir -p /usr/share/icons/hicolor/32x32/apps/  
RUN mkdir -p /usr/share/icons/hicolor/48x48/apps/  
RUN mkdir -p /usr/share/icons/hicolor/128x128/apps/  
RUN mkdir -p /usr/share/icons/hicolor/256x256/apps/  
  
# Install Sublime Text 3 with Dependency  
RUN apt-get update && \  
apt-get install -y software-properties-common python-software-properties && \  
add-apt-repository ppa:webupd8team/sublime-text-3 && \  
apt-get update && \  
apt-get install -y sublime-text-installer && \  
apt-get install -y libglib2.0-dev libx11-dev libgtk2.0-0  
  
# Font problem  
RUN apt-get install -y x11-xkb-utils xfonts-100dpi xfonts-75dpi xfonts-
scalable xfonts-cyrillic xserver-xorg-core && \  
apt-get remove -y dbus  
  
# VNC - Password = 1234  
RUN apt-get install -y x11vnc xvfb && \  
mkdir ~/.vnc && \  
x11vnc -storepasswd 1234 ~/.vnc/passwd  
  
RUN bash -c 'echo "/usr/bin/subl" >> /.bashrc'  
  
# CMD x11vnc  
ENTRYPOINT ["x11vnc", "-forever", "-usepw", "-create"]  

