FROM fedora:21  
MAINTAINER Stas Rudakou "stas@garage22.net"  
RUN yum -y update; yum clean all;  
RUN yum -y install transmission-daemon  
  
ADD settings.json /var/lib/transmission/settings.json  
RUN mkdir -p /data/transmission/ && \  
chown -R transmission: /data/transmission/ && \  
mkdir -p /pub_data/transmission/ && \  
chown -R transmission: /pub_data/transmission/ && \  
chown transmission: /var/lib/transmission/settings.json  
  
VOLUME ["/data/transmission/", "/pub_data/transmission/"]  
  
EXPOSE 9091  
EXPOSE 12345  
USER transmission  
CMD bash -c "cp /var/lib/transmission/settings.json /data/transmission/. && \  
/usr/bin/transmission-daemon -f --no-portmap --log-info -g /data/transmission"  

