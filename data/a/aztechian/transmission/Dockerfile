FROM debian:jessie-slim  
  
ARG version=2.9.2  
ENV USERNAME="transmission" \  
PASSWORD="password" \  
DISPLAY=":0" \  
LANG="C.UTF-8" \  
DEBIAN_FRONTEND=noninteractive  
  
LABEL maintainer="Ian Martin <ian@imartin.net>" license="MIT" version=$version  
  
COPY settings.json /var/lib/transmission-daemon/  
COPY run.sh /  
  
RUN apt-get -q update && \  
apt-get install -qy --force-yes transmission-daemon ca-certificates wget tar
curl unrar-free procps && \  
apt-get -y autoremove && \  
apt-get -y clean && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /tmp/* && \  
chmod +x /run.sh && \  
mkdir -p /transmission && \  
chown -R debian-transmission: /transmission  
  
VOLUME ["/transmission"]  
EXPOSE 9091 45555  
USER debian-transmission  
ENTRYPOINT ["/run.sh"]  

