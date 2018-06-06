FROM debian:jessie  
  
MAINTAINER Michael Feller  
  
ENV TS_VERSION LATEST  
ENV LANG C.UTF-8  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get -y install bzip2 mariadb-client
libmariadb2 wget ca-certificates python3 \  
&& rm -rf /var/lib/apt/lists/* \  
&& useradd -M -s /bin/false \--uid 1000 teamspeak3 \  
&& mkdir -p /data/files \  
&& chown teamspeak3:teamspeak3 /data  
  
ADD ts3server.ini /data  
ADD ts3db_mariadb.ini /data  
ADD get-version.py /get-version  
ADD start-teamspeak3.sh /start-teamspeak3  
RUN chmod +x /start-teamspeak3  
  
EXPOSE 9987/udp 10011/tcp 30033/tcp  
  
USER teamspeak3  
VOLUME /data  
WORKDIR /data  
CMD ["/start-teamspeak3"]  

