FROM ubuntu:zesty  
  
# make apt non-interactive  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install dev tools & dependencies  
RUN \  
apt update && \  
apt install -y build-essential git cmake devscripts debhelper git-buildpackage
&& \  
apt install -y extra-cmake-modules qtbase5-dev libqt5x11extras5-dev
qtdeclarative5-dev && \  
apt install -y libkf5coreaddons-dev libkf5i18n-dev gettext libkf5dbusaddons-
dev libkf5globalaccel-dev libkf5config-dev libkf5xmlgui-dev && \  
apt install -y libkf5notifications-dev plasma-framework-dev kdoctools-dev && \  
apt install -y xserver-xorg-input-wacom libxrandr-dev libxi-dev  
  
COPY docker-build-internal.sh /root/  
WORKDIR /root  
  
ENTRYPOINT ["/bin/bash", "docker-build-internal.sh"]  

