FROM ubuntu:latest  
  
MAINTAINER Profenter  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN dpkg --add-architecture i386 \  
&& apt-get update \  
&& apt-get -y install tmux mailutils postfix curl lib32gcc1 libstdc++6
libstdc++6:i386 wget \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get clean  
RUN mkdir -p /opt/ark \  
&& useradd -d /opt/ark -s /bin/bash --uid 1000 arkserver \  
&& chown -R arkserver:arkserver /opt/ark  
  
EXPOSE 27015/udp 7778/udp  
EXPOSE 32330/tcp  
  
  
ADD arkserver /opt/ark/arkserver  
ADD start.sh /opt/ark/start.sh  
USER arkserver  
VOLUME /opt/ark/serverfiles  
WORKDIR /opt/ark  
CMD ./start.sh  

