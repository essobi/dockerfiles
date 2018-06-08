# x11docker/plasma  
#  
# Run KDE plasma desktop in docker.  
# Use x11docker to run image.  
# Get x11docker from github:  
# https://github.com/mviereck/x11docker  
#  
# Examples:  
# Desktop:  
# x11docker --desktop x11docker/plasma  
# Single application (terminal):  
# x11docker x11docker/plasma konsole  
# Single application in Wayland:  
# x11docker --wayland --dbus x11docker/plasma konsole  
#  
# Experimental Wayland desktop examples:  
# Plasma destop as nested Wayland compositor:  
# x11docker --hostdisplay --waylandenv --dbus --gpu x11docker/plasma
startplasmacompositor  
# Plasma Wayland session in kwin_wayland from host:  
# x11docker --kwin --wayland --dbus --gpu x11docker/plasma plasmashell  
#  
# Add hardware acceleration with option --gpu  
# Create a persistent home folder with option --home  
# Share clipboard with host with option --clipboard  
# Enable pulseaudio sound with option --pulseaudio  
#  
# See x11docker --help for further options.  
FROM debian:stretch  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update  
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
  
# base KDE with plasma and KWin  
RUN apt-get install -y --no-install-recommends kde-plasma-desktop kwin-x11  
  
# plasma compositor  
RUN apt-get install -y plasma-workspace-wayland \  
kwin-wayland-backend-wayland kwin-wayland-backend-x11  
  
# additional tools and styles  
RUN apt-get install -y at-spi2-core gtk3-engines-breeze \  
kate kcalc kde-config-screenlocker \  
kde-style-breeze-qt4 kde-style-qtcurve \  
kruler libqt5multimedia5-plugins pulseaudio psmisc \  
qt-at-spi qt5-gtk-platformtheme sound-theme-freedesktop \  
systemsettings vlc xdg-user-dirs  
  
# startscript to copy dotfiles from /etc/skel  
# runs either CMD or image command from docker run  
RUN echo '#! /bin/sh\n\  
[ -n "$HOME" ] && [ ! -e "$HOME/.config" ] && cp -R /etc/skel/. $HOME/ \n\  
exec $* \n\  
' > /usr/local/bin/start  
RUN chmod +x /usr/local/bin/start  
  
ENTRYPOINT ["/usr/local/bin/start"]  
CMD ["startkde"]  
  
ENV DEBIAN_FRONTEND newt  

