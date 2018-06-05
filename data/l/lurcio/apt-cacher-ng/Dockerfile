FROM ubuntu:16.04  
MAINTAINER margent@gmail.com  
  
ENV APT_CACHER_NG_CACHE_DIR=/var/cache/apt-cacher-ng \  
APT_CACHER_NG_LOG_DIR=/var/log/apt-cacher-ng \  
APT_CACHER_NG_USER=apt-cacher-ng  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y apt-cacher-ng \  
&& sed 's/# ForeGround: 0/ForeGround: 1/' -i /etc/apt-cacher-ng/acng.conf \  
&& echo 'PassThroughPattern: (packages-gitlab-
com\\.s3\\.amazonaws\\.com|packages-gitlab-
com\\.s3-accelerate\\.amazonaws\\.com|packages\\.gitlab\\.com|mirrors\\.fedoraproject\\.org):443'
>> /etc/apt-cacher-ng/acng.conf \  
&& echo 'VfilePatternEx: ^(/\?release=[0-9]+&arch=.*)$' >> /etc/apt-cacher-
ng/acng.conf \  
&& echo 'Remap-centos: file:centos_mirrors ;
http://mirror.ox.ac.uk/sites/mirror.centos.org/' >> /etc/apt-cacher-
ng/acng.conf \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY entrypoint.sh /sbin/entrypoint.sh  
RUN chmod 755 /sbin/entrypoint.sh  
  
COPY centos_mirrors /etc/apt-cacher-ng/centos_mirrors  
RUN chmod 644 /etc/apt-cacher-ng/centos_mirrors  
  
EXPOSE 3142/tcp  
VOLUME ["${APT_CACHER_NG_CACHE_DIR}"]  
ENTRYPOINT ["/sbin/entrypoint.sh"]  
CMD ["/usr/sbin/apt-cacher-ng"]  

