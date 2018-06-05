FROM ubuntu:16.04  
ENV DEBIAN_FRONTEND noninteractive  
ENV DELUGE_VERSION 1.3.15-1~xenial~ppa3  
  
# setup and install deluge (key: 249AD24C) from ppa  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 249AD24C \  
&& echo "deb http://ppa.launchpad.net/deluge-team/ppa/ubuntu xenial main" >
/etc/apt/sources.list.d/deluge.list \  
&& echo "deb http://archive.ubuntu.com/ubuntu/ xenial multiverse" >>
/etc/apt/sources.list \  
&& apt-get -q update \  
&& apt-get -y install supervisor \  
deluged=${DELUGE_VERSION} \  
deluge-web=${DELUGE_VERSION} \  
p7zip-full \  
unrar \  
unzip \  
&& rm -rf /var/lib/apt/lists/*  
  
# supervisor config  
COPY assets/configs/supervisor.conf /etc/supervisor/conf.d/deluge.conf  
  
VOLUME ["/data"]  
  
# torrent port (tcp and udp)  
EXPOSE 53160/tcp 53160/udp 8112/tcp 58846/tcp  
  
# kick off deluge|web  
ENTRYPOINT [ "/usr/bin/supervisord" ]  

