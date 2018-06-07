FROM ubuntu:14.04  
MAINTAINER Doro Wu <fcwu.tw@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV HOME /root  
  
# setup our Ubuntu sources (ADD breaks caching)  
RUN echo "deb http://tw.archive.ubuntu.com/ubuntu/ trusty main\n\  
deb http://tw.archive.ubuntu.com/ubuntu/ trusty multiverse\n\  
deb http://tw.archive.ubuntu.com/ubuntu/ trusty universe\n\  
deb http://tw.archive.ubuntu.com/ubuntu/ trusty restricted\n\  
deb http://ppa.launchpad.net/chris-lea/node.js/ubuntu trusty main\n\  
deb http://ppa.launchpad.net/lubuntu-dev/lubuntu-daily/ubuntu trusty main\n\  
"> /etc/apt/sources.list  
  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 20E36F2F C7917B12  
RUN apt-get update \  
&& apt-cache search lxqt|awk '$1 ~ /^lxqt/ {print $1}' | xargs apt-get install
-y \  
&& apt-get install -y --force-yes --no-install-recommends supervisor \  
pwgen sudo vim-tiny \  
net-tools \  
x11vnc xvfb \  
ttf-ubuntu-font-family \  
nodejs \  
&& apt-get autoclean \  
&& apt-get autoremove \  
&& rm -rf /var/lib/apt/lists/*  
  
ADD noVNC /noVNC/  
  
ADD startup.sh /  
ADD supervisord.conf /  
EXPOSE 6080  
EXPOSE 5900  
WORKDIR /  
ENTRYPOINT ["/startup.sh"]  

