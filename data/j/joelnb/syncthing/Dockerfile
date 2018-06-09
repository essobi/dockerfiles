FROM debian:jessie  
MAINTAINER Joel Noyce Barnham <joelnbarnham@gmail.com>  
  
# docker run -d --restart=always \  
# -v ~/.syncthing/:/config \  
# -v ~/Sync/:/data \  
# --hostname banana \  
# -p 22000:22000 -p 21025:21025/udp -p 127.0.0.1:8384:8384 \  
# --name syncthing \  
# joelnb/syncthing  
ARG SYNCTHING_VERSION=0.14.45  
RUN \  
export DEBIAN_FRONTEND=noninteractive && \  
apt-get update && \  
apt-get install curl ca-certificates -y --no-install-recommends && \  
curl -s https://syncthing.net/release-key.txt | apt-key add - && \  
echo "deb http://apt.syncthing.net/ syncthing release" >
/etc/apt/sources.list.d/syncthing-release.list && \  
apt-get update && \  
apt-get install syncthing=${SYNCTHING_VERSION} && \  
apt-get autoremove -y && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
:  
  
RUN \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 && \  
curl -o /usr/local/bin/gosu -SL
"https://github.com/tianon/gosu/releases/download/1.2/gosu-$(dpkg --print-
architecture)" && \  
curl -o /usr/local/bin/gosu.asc -L
"https://github.com/tianon/gosu/releases/download/1.2/gosu-$(dpkg --print-
architecture).asc" && \  
gpg --verify /usr/local/bin/gosu.asc && \  
rm /usr/local/bin/gosu.asc && \  
chmod +x /usr/local/bin/gosu && \  
:  
  
ARG uid=1000  
RUN useradd --no-create-home -g users -u "$uid" syncthing  
ENV STNOUPGRADE=1  
VOLUME ["/config", "/data"]  
EXPOSE 8384 22000 21025/udp  
  
COPY entrypoint.sh /opt/entrypoint.sh  
ENTRYPOINT ["/opt/entrypoint.sh"]  

