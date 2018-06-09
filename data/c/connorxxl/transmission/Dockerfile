FROM ubuntu:xenial  
  
MAINTAINER connorxxl <christian.flaig@gmail.com>  
  
RUN apt-get update && \  
apt-get install -y software-properties-common && \  
add-apt-repository -y ppa:transmissionbt/ppa && \  
apt-get update && \  
apt-get install -y transmission-daemon && \  
apt-get -y autoremove && \  
apt-get -y clean  
  
ENV GROUPID=1100  
ENV USERID=1100  
  
RUN groupadd -g $GROUPID transmission && useradd -u $USERID -g transmission
transmission  
  
RUN mkdir -p /config && chown -R transmission:transmission /config && \  
mkdir -p /volumes/complete && chown -R transmission:transmission
/volumes/complete && \  
mkdir -p /volumes/incomplete && chown -R transmission:transmission
/volumes/incomplete && \  
mkdir -p /volumes/watch && chown -R transmission:transmission /volumes/watch  
  
EXPOSE 9091 51414/tcp 51414/udp  
  
VOLUME ["/config"]  
VOLUME ["/volumes/complete"]  
VOLUME ["/volumes/incomplete"]  
VOLUME ["/volumes/watch"]  
  
USER transmission  
  
ENV TRANSMISSION_HOME /config  
  
ENTRYPOINT ["/usr/bin/transmission-daemon"]  
CMD [ "--allowed", "*.*.*.*", "--encryption-preferred", "--foreground", "--
dht", "--no-auth", "--watch-dir", "/volumes/watch", "--incomplete-dir",
"/volumes/incomplete", "--download-dir", "/volumes/complete" ]  

