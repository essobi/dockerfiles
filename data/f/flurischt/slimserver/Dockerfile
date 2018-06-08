FROM ubuntu:xenial  
  
ENV BRANCH "public/7.9"  
RUN useradd -d "/home/slimserver" -m -s /bin/bash slimserver  
  
RUN \  
apt-get clean && \  
apt-get update && \  
apt-get dist-upgrade -y && \  
apt-get install -y curl wget faad flac lame sox libio-socket-ssl-perl git  
  
ADD startup.sh /  
RUN chmod +x /startup.sh  
  
WORKDIR /home/slimserver  
USER slimserver  
  
RUN \  
mkdir library && \  
git clone https://github.com/Logitech/slimserver.git && \  
cd slimserver && \  
git checkout $BRANCH  
  
RUN mkdir -p /home/slimserver/slimserver/docker_volume/Cache && ln -s
/home/slimserver/slimserver/docker_volume/Cache
/home/slimserver/slimserver/Cache  
RUN mkdir -p /home/slimserver/slimserver/docker_volume/prefs && ln -s
/home/slimserver/slimserver/docker_volume/prefs
/home/slimserver/slimserver/prefs  
  
EXPOSE 3483 3483/udp 9000 9090  
VOLUME /home/slimserver/slimserver/docker_volume  
  
CMD ["/startup.sh"]  

