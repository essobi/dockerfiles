FROM ubuntu:trusty  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update \  
&& apt-get dist-upgrade -y \  
&& apt-get clean  
  
RUN locale-gen en_US.UTF-8 fr_FR.UTF-8\  
&& echo "deb http://archive.ubuntu.com/ubuntu/ trusty-backports main
restricted universe multiverse" >> /etc/apt/sources.list \  
&& apt-get update \  
&& apt-get install -y wesnoth-1.12-server wget \  
&& apt-get clean \  
&& mkdir -p /var/run/wesnothd \  
&& mkdir -p /srv/wesnoth  
  
RUN wget
https://github.com/jwilder/dockerize/releases/download/v0.0.2/dockerize-linux-
amd64-v0.0.2.tar.gz \  
&& tar -C /usr/local/bin -xzvf dockerize-linux-amd64-v0.0.2.tar.gz \  
&& rm dockerize-linux-amd64-v0.0.2.tar.gz  
  
ADD wesnothd.cfg.tmpl /etc/  
  
ENV REPLAYS true  
ENV THREADS 5  
ENV MOTD Welcome to this game server  
EXPOSE 15000  
  
CMD /usr/local/bin/dockerize -template
/etc/wesnothd.cfg.tmpl:/etc/wesnothd.cfg \  
/usr/games/wesnothd-1.12 -c /etc/wesnothd.cfg \--threads $THREADS  

