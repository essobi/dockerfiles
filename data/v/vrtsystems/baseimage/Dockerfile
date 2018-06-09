# vim:set ft=dockerfile:  
  
FROM debian:jessie  
MAINTAINER VRT Engineering <engineering@vrt.com.au>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV VER_GOSU 1.4  
  
# Add in a script to clean up afterwards (also for subsequent layers)  
COPY docker-cleanup.sh /usr/local/sbin/docker-cleanup.sh  
  
# grab gosu for easy step-down from root  
RUN gpg --keyserver pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4  
RUN apt-get update && apt-get install -y curl git openssh-client locales
supervisor apt-utils\  
&& echo "=== Setting locale =================================" \  
&& localedef -i en_AU -c -f UTF-8 -A /usr/share/locale/locale.alias
en_AU.UTF-8 \  
&& echo "=== Setting up 'gosu' ==============================" \  
&& curl -o /usr/local/bin/gosu -SL
"https://github.com/tianon/gosu/releases/download/$VER_GOSU/gosu-$(dpkg
--print-architecture)" \  
&& curl -o /usr/local/bin/gosu.asc -SL
"https://github.com/tianon/gosu/releases/download/$VER_GOSU/gosu-$(dpkg
--print-architecture).asc" \  
&& gpg \--verify /usr/local/bin/gosu.asc \  
&& rm /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& echo "=== Setting up 'supervisor' ========================" \  
&& mkdir -p /var/log/supervisor \  
&& echo "=== Setting up 'openssh-client' ====================" \  
&& mkdir -p /root/.ssh \  
&& ssh-keyscan -H github.com >> /root/.ssh/known_hosts \  
&& ssh-keyscan -H bitbucket.org >> /root/.ssh/known_hosts \  
&& echo "=== Cleaning up ========================" \  
&& /usr/local/sbin/docker-cleanup.sh  
  
ENV LANG en_AU.utf8  
  
# In images derived from this one...  
# COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
# CMD ["/usr/bin/supervisord"]  

