FROM combro2k/debian-debootstrap:8  
MAINTAINER Martijn van Maurik <docker@vmaurik.nl>  
  
ENV VERSION 0.14.26  
ADD start.sh /usr/local/bin/run  
  
RUN useradd syncthing -b /config && \  
export DEBIAN_FRONTEND=noninteractive && \  
apt-get update && apt-get install tar curl ca-certificates sudo -yq && \  
mkdir -p /opt/syncthing && cd /opt/syncthing && \  
curl -k -L
https://github.com/syncthing/syncthing/releases/download/v${VERSION}/syncthing-
linux-amd64-v${VERSION}.tar.gz | tar zxv --strip-components=1 && \  
mkdir -p /config /data && chown -R syncthing:syncthing /data /config && \  
chmod +x /usr/local/bin/run && chown -R syncthing:syncthing /opt/syncthing  
  
WORKDIR /opt/syncthing  
  
EXPOSE 8080 22000/tcp 22000/udp  
  
VOLUME ["/data", "/config"]  
  
CMD ["/usr/local/bin/run"]  

