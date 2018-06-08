FROM ubuntu:16.04  
MAINTAINER BK Box "bk@theboxes.org"  
  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv 06E85760C0A52C50; \  
echo "deb http://www.ubnt.com/downloads/unifi/debian stable ubiquiti" | tee -a
/etc/apt/sources.list; \  
apt-get -y update; \  
apt-get -y upgrade; \  
apt-get -y install \  
unifi  
  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD run.sh /usr/lib/unifi/  
  
EXPOSE 8080 8443 8843 8880  
EXPOSE 27117  
EXPOSE 3478/udp  
VOLUME ["/var/lib/unifi"]  
  
WORKDIR /usr/lib/unifi  
ENTRYPOINT ["/usr/lib/unifi/run.sh"]  

