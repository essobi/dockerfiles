# A LAMP image based on Turnkeylinux  
# forked from adminrezo/docker-lamp  
FROM turnkeylinux/lamp-14.0  
MAINTAINER Christian Boulanger "info@bibliograph.org"  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Upgrades / Repos  
RUN (apt-get update && apt-get upgrade -y -q && apt-get dist-upgrade -y -q &&
apt-get -y -q autoclean && apt-get -y -q autoremove)  
RUN apt-get install -y supervisor  
  
# Starting services  
RUN mkdir -p /var/log/supervisor  
ADD supervisor-lamp.conf /etc/supervisor/conf.d/supervisor-lamp.conf  
ADD start.sh /start.sh  
EXPOSE 443 80  
CMD ["/start.sh"]  

