FROM debian:jessie-backports  
MAINTAINER Voobscout <voobscout@gmail.com>  
  
ENV HOME /root  
ADD http://repo.yandex.ru/yandex-disk/yandex-disk_latest_amd64.deb /tmp  
ADD https://github.com/Yelp/dumb-init/releases/download/v1.2.1/dumb-
init_1.2.1_amd64.deb /tmp  
  
RUN export DEBIAN_FRONTEND='noninteractive' && \  
export GIT_SSL_NO_VERIFY=1 && \  
export container=docker && \  
apt -y update && apt -fy dist-upgrade && \  
apt -fy install wget expect procps && \  
dpkg -i /tmp/yandex-disk_latest_amd64.deb && \  
dpkg -i /tmp/dumb-init_1.2.1_amd64.deb  
  
RUN apt-get -y autoremove && apt-get -yq clean && \  
rm -rf /var/lib/{apt,dpkg,cache,log}/ \  
/tmp/* \  
/var/log/apt/* \  
/var/log/alternatives.log \  
/var/log/bootstrap.log \  
/var/log/dpkg.log  
  
ADD start.sh /  
ENTRYPOINT ["/usr/bin/dumb-init", "/start.sh"]  

