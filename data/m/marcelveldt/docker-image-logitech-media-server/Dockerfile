FROM debian:jessie  
MAINTAINER Marcel van der Veldt <m.vanderveldt@outlook.com>  
  
RUN groupadd -g 1024 100 && \  
useradd -u 1024 -g 100 admin  
  
ENV SQUEEZE_VOL /mnt/config  
ENV LANG C.UTF-8  
ENV DEBIAN_FRONTEND noninteractive  
ENV
PACKAGE_VERSION_URL=http://www.mysqueezebox.com/update/?version=7.9.1&revision=1&geturl=1&os=deb  
  
RUN apt-get update && \  
apt-get -y --force-yes install curl sudo faad flac lame sox libio-socket-ssl-
perl && \  
url=$(curl "$PACKAGE_VERSION_URL" | sed 's/_all\\.deb/_amd64\\.deb/') && \  
curl -Lsf -o /tmp/logitechmediaserver.deb $url && \  
dpkg -i /tmp/logitechmediaserver.deb && \  
rm -f /tmp/logitechmediaserver.deb && \  
apt-get clean  
  
VOLUME $SQUEEZE_VOL  
EXPOSE 3483 3483/udp 9000 9090  
COPY entrypoint.sh /entrypoint.sh  
COPY start-squeezebox.sh /start-squeezebox.sh  
RUN chmod 755 /entrypoint.sh /start-squeezebox.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  

