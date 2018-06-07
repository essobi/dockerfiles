FROM debian:9-slim  
MAINTAINER FallDawn <QiuFengXiaoShi@Gmail.Com>  
  
ADD https://download-cdn.resilio.com/2.5.12/linux-x64/resilio-sync_x64.tar.gz
/tmp/resilio-sync.tgz  
ADD start.sh /usr/local/bin/start  
  
RUN tar -xf /tmp/resilio-sync.tgz -C /usr/local/bin/ rslsync && rm -f
/tmp/resilio-sync.tgz  
RUN useradd docker && sed -e "s/docker:x:1000:1000/docker:x:0:0/" -i
/etc/passwd  
  
EXPOSE 8888  
EXPOSE 55555  
VOLUME /home/docker/resilio-sync-config /home/docker/resilio-sync-storage
/mnt/resilio-sync  
  
ENTRYPOINT ["start"]

