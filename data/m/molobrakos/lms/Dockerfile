FROM debian:stable-slim  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV LANG C.UTF-8  
  
VOLUME /config /music /logs /cache  
  
WORKDIR /lms  
  
RUN apt-get update && \  
apt-get -y install curl pv supervisor faad flac lame sox libio-socket-ssl-perl
dumb-init && \  
curl -O \  
http://downloads-origin.slimdevices.com/nightly$(curl http://downloads-
origin.slimdevices.com/nightly/?ver=7.9 | grep -o '/7.9[^"]*amd64.deb') && \  
dpkg -i *.deb && \  
rm -f *.deb && \  
apt-get -y autoremove && \  
apt-get -y clean && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /tmp/* && \  
rm -rf /var/tmp/* && \  
useradd \--user-group \--home-dir /lms \--shell /bin/false lms  
  
EXPOSE 3483 3483/udp 9000 9090  
  
HEALTHCHECK CMD curl \--max-time 5 \--silent \--fail \--output /dev/null
\--data '{"id":1,"method":"slim.request","params":["",["serverstatus"]]}'
http://localhost:9000/jsonrpc.js || exit 1  
  
USER lms  
  
ENTRYPOINT [ "dumb-init", "--", "squeezeboxserver", "--user", "lms", "--
prefsdir", "/config", "--logdir", "/logs", "--cachedir", "/cache" ]  

