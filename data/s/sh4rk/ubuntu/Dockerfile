FROM ubuntu:trusty  
MAINTAINER Felix Seidel <felix@seidel.me>  
  
ENV DEBIAN_FRONTEND noninteractive  
ADD config /config  
ADD root /root  
  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y nano supervisor wget ca-certificates patch && \  
apt-get clean && rm -rf /var/lib/apt/lists/* && \  
dpkg-divert --local \--rename /etc/supervisor/supervisor.conf && \  
mkdir -p /config /data && \  
chmod +x /config/loop && \  
groupadd --gid 500 core && \  
useradd --uid 500 --gid core core && \  
chown core:core /data  
  
ADD etc /etc  
  
VOLUME /data  
CMD ["/bin/bash", "/config/loop"]  

