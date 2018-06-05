FROM debian:jessie  
  
MAINTAINER aheil  
  
ENV TS_VERSION LATEST  
ENV LANG C.UTF-8  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get -y install bzip2 wget ca-
certificates \  
&& rm -rf /var/lib/apt/lists/* \  
&& useradd -M -s /bin/false \--uid 1000 teamspeak3 \  
&& mkdir /data \  
&& chown teamspeak3:teamspeak3 /data  
  
COPY get-version.sh /get-version  
COPY start-teamspeak3.sh /start-teamspeak3  
  
EXPOSE 9987/udp 10011 30033  
USER teamspeak3  
VOLUME /data  
WORKDIR /data  
CMD ["/start-teamspeak3"]  
  

