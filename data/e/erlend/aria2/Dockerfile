FROM alpine:3.5  
# Aria2 RPC port  
EXPOSE 6800  
# BitTorernt TCP listen port  
EXPOSE 6881/tcp  
# BitTorernt UDP listen port (used by DHT)  
EXPOSE 6881/udp  
  
VOLUME /config  
  
ENV ARIA2_GID=1000 ARIA2_UID=1000  
RUN apk add --no-cache aria2 openssl dumb-init su-exec  
  
COPY entrypoint.sh /  
COPY startup/* /etc/startup/  
COPY aria2.conf /etc/  
  
ENTRYPOINT ["/entrypoint.sh"]  

