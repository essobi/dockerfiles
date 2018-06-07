FROM debian:9-slim  
MAINTAINER FallDawn <QiuFengXiaoShi@Gmail.Com>  
  
# install  
ADD
https://github.com/syncthing/syncthing/releases/download/v0.14.46/syncthing-
linux-amd64-v0.14.46.tar.gz /tmp/syncthing.tgz  
ADD start.sh /usr/local/bin/start  
  
RUN tar -xf /tmp/syncthing.tgz -C /tmp syncthing-linux-
amd64-v0.14.46/syncthing && mv /tmp/syncthing-linux-amd64-v0.14.46/syncthing
/usr/local/bin/ && \  
rm -rf /tmp/syncthing.tgz /tmp/syncthing-linux-amd64-v0.14.46  
RUN useradd docker && sed -e "s/docker:x:1000:1000/docker:x:0:0/" -i
/etc/passwd  
  
EXPOSE 8384/tcp  
EXPOSE 22000/tcp  
EXPOSE 21027/udp  
  
VOLUME /home/docker/syncthing-config /mnt/syncthing-sync  
  
ENTRYPOINT ["start"]

