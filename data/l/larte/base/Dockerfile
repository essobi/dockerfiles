FROM debian:7.6  
MAINTAINER larte  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && apt-get -y install apt-utils locales wget && \  
echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen && \  
locale-gen && \  
/usr/sbin/update-locale LANG=en_US.UTF-8 && \  
apt-get clean && rm -Rf /var/cache/apt  
ENV LC_ALL en_US.UTF-8  

