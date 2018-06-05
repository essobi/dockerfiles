FROM debian:9  
RUN \  
groupadd -g 666 mybackup && \  
useradd -u 666 -g 666 -d /backup -c "MySQL Backup User" mybackup  
  
RUN \  
apt-get -y update && \  
apt-get -y install mydumper zstd && \  
rm -rf /var/lib/apt/lists/*  
  
COPY init.sh /init.sh  
RUN chmod 750 /init.sh  
  
VOLUME ["/backup"]  
WORKDIR /backup  
  
CMD ["/init.sh"]  

