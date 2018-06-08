# x11docker/mate  
#  
# Run Mate desktop in docker.  
# Use x11docker to run image.  
# Get x11docker from github:  
# https://github.com/mviereck/x11docker  
#  
# Examples: x11docker --desktop x11docker/mate  
# x11docker x11docker/mate caja  
#  
# Options:  
# Persistent home folder stored on host with --home  
# Shared host folder with --sharedir DIR  
# Hardware acceleration with option --gpu  
# Clipboard sharing with option --clipboard  
# Sound support with option --alsa or --pulseaudio  
#  
# See x11docker --help for further options.  
FROM debian:stretch  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-mark hold iptables && \  
apt-get -y dist-upgrade && apt-get autoremove -y && apt-get clean  
RUN apt-get install -y dbus-x11 procps psmisc  
  
# OpenGL / MESA  
RUN apt-get install -y mesa-utils mesa-utils-extra libxv1 kmod xz-utils  
  
# Language/locale settings  
# replace en_US by your desired locale setting,  
# for example de_DE for german.  
ENV LANG en_US.UTF-8  
RUN echo $LANG UTF-8 > /etc/locale.gen  
RUN apt-get install -y locales && update-locale --reset LANG=$LANG  
  
# some utils to have proper menus, mime file types etc.  
RUN apt-get install -y --no-install-recommends xdg-utils xdg-user-dirs \  
menu menu-xdg mime-support desktop-file-utils  
  
# Mate desktop core  
RUN apt-get install -y --no-install-recommends mate-desktop-environment-core  
  
# additional goodies  
RUN apt-get install -y fortunes mate-applets mate-notification-daemon \  
mate-system-monitor mate-utils  
  
# startscript to copy dotfiles from /etc/skel  
# runs either CMD or image command from docker run  
RUN echo '#! /bin/sh\n\  
[ -e "$HOME/.config" ] || cp -R /etc/skel/. $HOME/ \n\  
exec $* \n\  
' > /usr/local/bin/start  
RUN chmod +x /usr/local/bin/start  
  
ENTRYPOINT ["/usr/local/bin/start"]  
CMD ["mate-session"]  
  
ENV DEBIAN_FRONTEND newt  
  
  

