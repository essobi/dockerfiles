FROM ubuntu:15.10  
MAINTAINER Alessio Deiana <adeiana@gmail.com>  
  
RUN apt-get update && \  
apt-get -qq install debhelper wget  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN wget http://switch.dl.sourceforge.net/sourceforge/hd-idle/hd-idle-1.05.tgz  
RUN tar xvfz hd-idle-*.tgz  
RUN cd hd-idle && dpkg-buildpackage -rfakeroot  
RUN dpkg -i hd-idle_*.deb  
  
CMD /usr/sbin/hd-idle -d -i 600

