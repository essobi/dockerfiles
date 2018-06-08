FROM debian:wheezy  
  
MAINTAINER gregory "greg2502@gmail.com"  
RUN echo 'deb http://files.freeswitch.org/repo/deb/debian/ wheezy main' >>
/etc/apt/sources.list.d/freeswitch.list  
RUN gpg --keyserver pool.sks-keyservers.net --recv-key D76EDC7725E010CF  
RUN gpg -a --export D76EDC7725E010CF | apt-key add -  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update -y -qq && apt-get install -y -qq freeswitch-meta-vanilla \  
freeswitch-mod-shout freeswitch-mod-rayo  
ENV DEBIAN_FRONTEND dialog  
  
RUN cp -a /usr/share/freeswitch/conf/vanilla/ /etc/freeswitch  
  
WORKDIR /etc/freeswitch  
VOLUME ['/etc/freeswitch/']  
EXPOSE 8021  
CMD /usr/bin/freeswitch -c  

