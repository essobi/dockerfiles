FROM alpine:3.5  
LABEL os=alpine  
LABEL app=transmission  
ENV RPC_PORT 9091  
ENV PEER_PORT 54321  
ADD files/rootfs /  
RUN apk add --no-cache transmission-daemon && \  
mkdir -m 1777 /torrents  
VOLUME /torrents  
EXPOSE $RPC_PORT $PEER_PORT  
CMD ["/opt/transmission/transmission"]  

