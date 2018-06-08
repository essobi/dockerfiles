FROM debian:jessie  
  
MAINTAINER Alexander Mustafin <mustafin.aleksandr@gmail.com>  
  
#Grab keys for repo  
RUN apt-key adv --keyserver keys.gnupg.net --recv-key 9CEBFFC569A832B6  
  
#Add repo and install packets  
RUN echo 'deb http://pkg.yeti-switch.org/debian/jessie unstable main ext' >>
/etc/apt/sources.list && \  
apt-get update && apt-get -y install yeti-management && rm -rf
/var/lib/apt/lists/*  
  
VOLUME ["/etc/yeti/", "/var/log/yeti"]  
  
COPY management.cfg system.cfg /etc/yeti/  
  
EXPOSE 4444  
CMD ["/usr/bin/yeti_management", "-f"]  

