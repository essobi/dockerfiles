FROM debian:jessie  
  
MAINTAINER Kevin Coffey <kevdougful@gmail.com>  
  
RUN apt-get update && \  
apt-get install -y \  
deluged \  
deluge-web \  
&& rm -rf /var/lib/apt/lists/* && \  
apt-get clean  
  
# Add deluge system user  
RUN adduser --system \  
\--gecos "Deluge Service" \  
\--disabled-password \  
\--group \  
\--home /var/lib/deluge \  
deluge  
  
ENV DELUGED_USER=deluge \  
DELUGED_PASS=deluge  
  
VOLUME /progress \  
/complete \  
/autoadd \  
/torrents \  
/var/log/deluge  
  
RUN mkdir /var/lib/deluge/state  
  
COPY start.sh /var/lib/deluge/  
COPY *.conf /var/lib/deluge/  
  
RUN mkdir -p /var/log/deluge && \  
mkdir -p /var/lib/deluge/state && \  
chown -R deluge:deluge /var/lib/deluge && \  
chown -R deluge:deluge /var/log/deluge && \  
chmod -R 750 /var/log/deluge && \  
chmod 755 /var/lib/deluge/start.sh  
  
EXPOSE 58846/tcp \  
53160/tcp \  
53160/udp \  
8112/tcp  
  
USER deluge  
  
CMD ["/var/lib/deluge/start.sh"]  

