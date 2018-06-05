# GrooveBasin image  
# ORIGINAL MAINTAINER Simon Morvan garphy@zone84.net  
# Modified to use stackbrew and remove supervisord  
# use stackbrew's super-small ubuntu  
FROM stackbrew/ubuntu:14.04  
MAINTAINER John Regan john@jrjrtech.com  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get install -y software-properties-common && \  
apt-add-repository ppa:andrewrk/libgroove && \  
apt-add-repository ppa:chris-lea/node.js && \  
apt-get update  
  
RUN apt-get -y install build-essential git python && \  
apt-get -y install libgroove-dev libgrooveplayer-dev \  
libgrooveloudness-dev libgroovefingerprinter-dev \  
libgroove4 libgrooveplayer4 libgrooveloudness4 libgroovefingerprinter4 && \  
apt-get -y install nodejs  
  
RUN useradd -m groovebasin -G audio && \  
mkdir /music && touch /music/.dummy && \  
chown groovebasin:groovebasin /music && \  
mkdir /groove && touch /groove/.dummy && \  
chown groovebasin:groovebasin /groove  
  
RUN ln -s /music /home/groovebasin/music && \  
ln -s /groove /home/groovebasin/groovebasin.db && \  
chown groovebasin:groovebasin /home/groovebasin/*  
  
ADD build.sh /tmp/build.sh  
RUN /tmp/build.sh  
  
RUN apt-get -y remove libgroove-dev libgrooveplayer-dev \  
libgrooveloudness-dev libgroovefingerprinter-dev \  
manpages manpages-dev g++ gcc cpp make ucf \  
python-software-properties unattended-upgrades \  
g++ gcc cpp build-essential git python  
  
RUN apt-get -y autoremove  
  
USER groovebasin  
ENV HOME /home/groovebasin  
WORKDIR /home/groovebasin  
RUN ln -s /music /home/groovebasin/music && \  
ln -s /groove /home/groovebasin/groovebasin.db  
  
EXPOSE 16242  
EXPOSE 6600  
VOLUME /music  
VOLUME /groove  
  
ENTRYPOINT ["node","/home/groovebasin/groovebasin-build/lib/server.js"]  

