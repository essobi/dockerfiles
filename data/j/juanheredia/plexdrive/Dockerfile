FROM ubuntu:16.04  
LABEL maintainer="jchm@infoinnova.net"  
  
COPY install.sh /install.sh  
RUN chmod +x /install.sh  
RUN /install.sh  
  
COPY entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
  
ENV MOUNTPOINT="/mnt/mountpoint" \  
CACHE_SIZE=100 \  
MAX_CHUNKS=100 \  
VERBOSITY=2 \  
REFRESH=60m  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["mount"]  

