FROM alpine:3.4  
ENV TRANSMISSION_VERSION 2.92-r2  
  
RUN apk add --no-cache transmission-daemon==${TRANSMISSION_VERSION}  
  
EXPOSE 9091  
VOLUME /data  
  
ENV CONFIG_DIR /data/.config  
ENV INCOMPLETE_DIR /data/.incomplete  
ENV WATCH_DIR /data/.watch  
ENV DOWNLOAD_DIR /data/new  
  
ENV LOG_LEVEL info  
ENV RPC_ADDRESS 0.0.0.0  
ENV RPC_WHITELIST 127.*.*.*,172.17.*.*,192.168.*.*  
ENV ENCRYPTION required  
ENV EXTRA_ARGS --paused  
  
COPY init /srv/init  
  
CMD [ "/srv/init" ]  

