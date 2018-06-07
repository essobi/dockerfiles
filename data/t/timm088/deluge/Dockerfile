FROM alpine:3.6  
  
RUN apk -U upgrade && \  
apk add --no-cache \  
ca-certificates \  
p7zip \  
unzip \  
unrar \  
curl \  
tzdata \  
py-pip && \  
apk add --no-cache --repository http://dl-cdn.alpinelinux.org/alpine/edge/main
\  
libressl && \  
apk add --no-cache --repository http://dl-
cdn.alpinelinux.org/alpine/edge/testing \  
deluge && \  
\  
pip install \  
service_identity \  
incremental \  
constantly \  
automat  
  
COPY ./deluge_start.sh /deluge_start.sh  
  
RUN adduser -u 1001 -S media -G users && \  
mkdir /data /movies /downloads /comics /tvseries && \  
chown -R media:users /data /movies /downloads /tvseries /comics && \  
chmod +x /deluge_start.sh && \  
chown media:users /deluge_start.sh  
  
#two processes running kind of goes against the docker mentality  
#would prefer if i could split the daemon and the web front-end but this
relies on the app  
#For now, a simple shell script works fine  
  
EXPOSE 53160 8112 58846  
EXPOSE 53160/udp  
  
USER media  
  
VOLUME ["/data", "/movies", "/tvseries", "/downloads", "/comics"]  
  
CMD ["/deluge_start.sh"]  

