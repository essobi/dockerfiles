FROM ubuntu:14.04  
MAINTAINER graham@grahamc.com  
  
ADD http://download-lb.utorrent.com/endpoint/btsync/os/linux-x64/track/stable
/tmp/btsync.tar.gz  
  
RUN adduser --system --disabled-password --disabled-login --uid 9001 btsync  
RUN mkdir /var/run/btsync/ /var/cache/btsync  
RUN chown btsync /var/run/btsync /var/cache/btsync  
  
RUN mkdir -p /opt/btsync  
RUN tar -zvvxf /tmp/btsync.tar.gz -C /opt/btsync  
RUN rm /tmp/btsync.tar.gz  
  
COPY 0conf/build /opt/btsync/build-conf  
COPY 0conf/start /opt/btsync/start  
  
RUN mkdir -p /mount/data /mount/config  
RUN chown btsync /mount/data /mount/config  
VOLUME ["/mount/data", "/mount/config"]  
EXPOSE 3369  
EXPOSE 3369/udp  
EXPOSE 8888  
USER btsync  
ENV BTSYNC_NAME docker-btsync  
  
CMD ["/opt/btsync/start"]  
  

