FROM alpine  
MAINTAINER Christian Gatzlaff "cgatzlaff@gmail.com"  
RUN apk add --no-cache rsync bash  
  
ENV RSYNC_TIMEOUT 300  
ENV RSYNC_MAX_CONNECTIONS 10  
ENV RSYNC_PORT 873  
ENV VOL /vol  
  
EXPOSE ${RSYNC_PORT}  
  
COPY server.sh /server.sh  
RUN chmod 755 /server.sh && \  
mkdir ${VOL} && \  
chmod 755 ${VOL}  
  
VOLUME ${VOL}  
  
ENTRYPOINT ["/server.sh"]

