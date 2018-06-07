FROM ubuntu  
ENV VERSION 2.1.19  
RUN DEBIAN_FRONTEND=noninteractive apt-get update \  
&& apt-get install -y \  
&& apt-get clean \  
&& useradd -u 1911 -U -d /config -s /bin/false jjs \  
&& usermod -G users jjs  
  
ADD https://github.com/just-
containers/s6-overlay/releases/download/v1.20.0.0/s6-overlay-amd64.tar.gz
/tmp/  
RUN gunzip -c /tmp/s6-overlay-amd64.tar.gz | tar -xf - -C /  
  
ADD https://www.urbackup.org/downloads/Server/2.1.19/urbackup-
server_2.1.19_amd64.deb /root/urbackup.deb  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y /root/urbackup.deb  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y -f  
  
#ADD backupfolder /etc/urbackup/backupfolder  
#RUN chmod +x /etc/urbackup/backupfolder  
EXPOSE 55413  
EXPOSE 55414  
EXPOSE 55415  
EXPOSE 35623  
COPY root/ /  
  
VOLUME [ "/var/urbackup", "/var/log", "/backup"]  
ENTRYPOINT ["/init"]  

