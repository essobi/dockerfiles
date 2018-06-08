FROM alpine  
MAINTAINER add <ohmyadd@gmail.com>  
  
RUN apk add --no-cache git build-base linux-headers wireless-tools && \  
git clone https://github.com/wi-fi-analyzer/mdk3-master.git /mdk3 && \  
cd mdk3 && \  
make && \  
make install && \  
rm -rf /mdk3 && \  
apk del git build-base linux-headers && \  
rm -rf /var/cache/*  
  
CMD sleep 1024d  

