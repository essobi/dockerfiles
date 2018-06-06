FROM ubuntu:xenial  
MAINTAINER Andrey Arapov <andrey.arapov@nixaid.com>  
  
# To avoid problems with Dialog and curses wizards  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get -y --no-install-recommends install ca-certificates wget git \  
openssh-client sudo libpulse0 \  
build-essential qmlscene \  
qt5-qmake qt5-default qtdeclarative5-dev qtdeclarative5-controls-plugin \  
qtdeclarative5-qtquick2-plugin libqt5qml-graphicaleffects \  
qtdeclarative5-dialogs-plugin qtdeclarative5-localstorage-plugin \  
qtdeclarative5-window-plugin && \  
rm -rf /var/lib/apt/lists/*  
  
ENV DUSER user  
ENV DGROUPS video,audio  
ENV DUID 1000  
ENV DHOME /home/$DUSER  
ENV APPDIR /opt/cool-retro-term  
  
RUN useradd -u $DUID -m -d $DHOME -s /usr/sbin/nologin -G $DGROUPS $DUSER && \  
mkdir -p $APPDIR && \  
chown -Rh $DUSER:$DUSER $APPDIR  
  
WORKDIR $DHOME  
USER $DUSER  
  
RUN git clone \--recursive https://github.com/Swordfish90/cool-retro-term.git
$APPDIR  
RUN cd $APPDIR && \  
qmake && \  
make -j $(nproc)  
  
USER root  
  
# You can install more apps you need here  
# E.g.:  
# RUN apt-get update && apt -y install pulseaudio-utils alsa-utils mplayer  
# Workaround: pulseaudio client library likes to remove /dev/shm/pulse-shm-*  
# files created by the host, causing sound to stop working.  
# To fix this, we either want to disable the shm or mount /dev/shm  
# in read-only mode when starting the container.  
RUN echo "enable-shm = no" | tee -a /etc/pulse/client.conf  
  
COPY launch /launch  
ENTRYPOINT [ "bash", "/launch" ]  

