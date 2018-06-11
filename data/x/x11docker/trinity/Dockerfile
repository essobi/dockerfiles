# x11docker/trinity  
#  
# Run trinity desktop environment in docker.  
# Use x11docker to run image.  
# Get x11docker from github:  
# https://github.com/mviereck/x11docker  
#  
# Examples: x11docker --desktop x11docker/trinity  
# x11docker x11docker/trinity konquerer  
#  
# Options:  
# Persistent home folder stored on host with --home  
# Shared host folder with --sharedir DIR  
# Hardware acceleration with option --gpu  
# Clipboard sharing with option --clipboard  
# Sound support with option --alsa or --pulseaudio  
# Language locale setting with --lang $LANG  
#  
# See x11docker --help for further options.  
FROM debian:jessie  
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
  
# Trinity desktop sources list  
RUN echo " \n\  
deb http://mirror.ppa.trinitydesktop.org/trinity/trinity-r14.0.0/debian jessie
main\n\  
deb-src http://mirror.ppa.trinitydesktop.org/trinity/trinity-r14.0.0/debian
jessie main\n\  
deb http://mirror.ppa.trinitydesktop.org/trinity/trinity-
builddeps-r14.0.0/debian jessie main\n\  
deb-src http://mirror.ppa.trinitydesktop.org/trinity/trinity-
builddeps-r14.0.0/debian jessie main \n\  
" >/etc/apt/sources.list.d/trinity.list  
  
# Trinity desktop installation. Remove tde-trinity to get tde-core-trinity
only  
RUN apt-get install -y gnupg && \  
apt-key adv --keyserver keyserver.quickbuild.io --recv-keys F5CFC95C && \  
apt-get update && \  
apt-get install -y --no-install-recommends tde-core-trinity && \  
apt-get install -y --no-install-recommends tde-trinity  
  
# startscript to copy dotfiles from /etc/skel  
# runs either CMD or image command from docker run  
RUN echo '#! /bin/sh\n\  
[ -n "$HOME" ] && [ ! -e "$HOME/.config" ] && cp -R /etc/skel/. $HOME/ \n\  
exec $* \n\  
' > /usr/local/bin/start  
RUN chmod +x /usr/local/bin/start  
  
ENV PATH="/opt/trinity/bin:$PATH"  
ENTRYPOINT ["/usr/local/bin/start"]  
CMD ["starttde"]  
  
ENV DEBIAN_FRONTEND newt  

