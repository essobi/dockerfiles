FROM debian:jessie-backports  
MAINTAINER Voobscout <voobscout@gmail.com>  
  
ENV HOME /root  
ADD http://repo.yandex.ru/yandex-disk/yandex-disk_latest_i386.deb /tmp  
ADD https://github.com/Yelp/dumb-init/archive/v1.2.1.tar.gz /tmp  
  
RUN export DEBIAN_FRONTEND='noninteractive' && \  
export GIT_SSL_NO_VERIFY=1 && \  
export container=docker && \  
dpkg --add-architecture i386 && \  
apt -y update && apt -fy dist-upgrade && \  
apt -fy install \  
wget \  
curl \  
build-essential \  
expect \  
procps \  
gcc-4.9-base:i386 \  
libc6:i386 \  
libc6-i686:i386 \  
libgcc1:i386 \  
libstdc++6:i386 \  
zlib1g:i386 \  
qemu-user-static && \  
dpkg -i /tmp/yandex-disk_latest_i386.deb && \  
rm -rf /etc/apt/sources.list.d/yandex-disk.list && \  
rm -rf /tmp/yandex-disk_latest_i386.deb  
  
RUN cd /tmp && \  
tar xzf v1.2.1.tar.gz && \  
cd /tmp/dumb-init-1.2.1 && \  
make -j$(nproc) && \  
cp /tmp/dumb-init-1.2.1/dumb-init /usr/bin/dumb-init && \  
cd / && \  
rm -rf /tmp/dumb-init-1.2.1  
  
RUN apt-get -yq remove build-essential && apt-get -y autoremove && apt-get -yq
clean && \  
rm -rf /var/lib/{apt,dpkg,cache,log}/ \  
/tmp/* \  
/var/log/apt/* \  
/var/log/alternatives.log \  
/var/log/bootstrap.log \  
/var/log/dpkg.log  
  
ADD start.sh /  
ENTRYPOINT ["/usr/bin/dumb-init", "/start.sh"]  

