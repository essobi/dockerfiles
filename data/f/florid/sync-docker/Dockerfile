# Resilio Sync  
#  
# VERSION 0.1  
#  
FROM ubuntu:latest  
MAINTAINER Resilio Inc. <support@resilio.com>  
LABEL com.resilio.version="2.5.13"  
  
ENV TZ 'Australia/Sydney'  
RUN echo $TZ > /etc/timezone && \  
apt-get update && apt-get install -y tzdata && \  
rm /etc/localtime && \  
ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \  
dpkg-reconfigure -f noninteractive tzdata && \  
apt-get clean  
  
ADD https://download-cdn.resilio.com/2.5.13/linux-x64/resilio-sync_x64.tar.gz
/tmp/sync.tgz  
RUN tar -xf /tmp/sync.tgz -C /usr/bin rslsync && rm -f /tmp/sync.tgz  
  
COPY sync.conf.default /etc/  
COPY run_sync /usr/bin/  
  
EXPOSE 8888  
EXPOSE 46098/tcp 46098/udp  
  
VOLUME /mnt/sync  
  
ENTRYPOINT ["run_sync"]  
CMD ["--config", "/mnt/sync/sync.conf"]  

