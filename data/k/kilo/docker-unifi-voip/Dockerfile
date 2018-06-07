FROM debian:jessie  
MAINTAINER fia5000  
  
VOLUME ["/var/lib/unifi-voip", "/var/log/unifi-voip", "/var/run/unifi-voip",
"/usr/lib/unifi-voip/work"]  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN echo "deb http://downloads-distro.mongodb.org/repo/debian-sysvinit dist
10gen" > \  
/etc/apt/sources.list.d/21mongodb.list && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv 7F0CEB10  
  
# Avoid ERROR: invoke-rc.d: policy-rc.d denied execution of start.  
# RUN echo "#!/bin/sh\nexit 101" > /usr/sbin/policy-rc.d  
RUN apt-get update && \  
apt-get install binutils jsvc mongodb-server wget -y && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN wget http://dl-origin.ubnt.com/unifi-
voip/1.0.6-vfy6nm/unifi_voip_sysvinit_all.deb && \  
dpkg -i unifi_voip_sysvinit_all.deb && \  
rm unifi_voip_sysvinit_all.deb  
  
RUN ln -s /var/lib/unifi-voip /usr/lib/unifi-voip/data  
EXPOSE 9080/tcp 9443/tcp  
  
WORKDIR /var/lib/unifi-voip  
  
ENTRYPOINT ["/usr/bin/java", "-Xmx1024M", "-jar", "/usr/lib/unifi-
voip/lib/ace.jar"]  
CMD ["start"]  
  

