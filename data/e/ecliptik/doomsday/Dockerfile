FROM ubuntu:16.04  
MAINTAINER Micheal Waltz <ecliptik@gmail.com>  
  
#Setup basic environment  
ENV DEBIAN_FRONTEND=noninteractive LANG=en_US.UTF-8 LC_ALL=C.UTF-8
LANGUAGE=en_US.UTF-8  
#Doomsday  
ENV DOOMSDAY=doomsday_2.0.0-build2068_amd64.deb  
ENV
DOOMSDAYURL=http://heanet.dl.sourceforge.net/project/deng/Doomsday%20Engine/Builds/$DOOMSDAY  
  
#Doom Shareware  
ENV DOOMWAD=doom1.wad  
ENV
DOOMURL=http://distro.ibiblio.org/pub/linux/distributions/slitaz/sources/packages/d/$DOOMWAD  
  
#DIR  
ENV WORKDIR=/app  
WORKDIR $WORKDIR  
RUN mkdir -p $WORKDIR  
  
#Download Doomsday and install  
RUN set -ex && \  
buildDeps=' \  
wget \  
' && \  
runDeps=' \  
libqt5gui5 \  
libqt5x11extras5 \  
libsdl2-mixer-2.0-0 \  
libxrandr2 \  
libxxf86vm1 \  
libfluidsynth1 \  
libqt5opengl5 \  
' && \  
apt-get update && \  
apt-get install -y --no-install-recommends $buildDeps $runDeps && \  
wget $DOOMSDAYURL -O $WORKDIR/$DOOMSDAY && \  
wget $DOOMURL -O $WORKDIR/$DOOMWAD && \  
dpkg --install $WORKDIR/$DOOMSDAY && \  
apt-get purge -y --auto-remove $buildDeps && \  
rm -rf /var/lib/apt/lists/* $WORKDIR/$DOOMSDAY  
  
#Copy files  
COPY . ${WORKDIR}  
  
#Open Doomsday port  
ENV PORT=13209  
EXPOSE $PORT  
  
#Run doomsday-server  
ENTRYPOINT [ "doomsday-server" ]  
CMD [ "--version" ]  

