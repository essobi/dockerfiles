FROM spira/docker-base  
  
MAINTAINER "Zak Henry" <zak.henry@gmail.com>  
  
  
RUN apt-get update -y && \  
apt-get install -y \  
git \  
curl \  
php5-cli \  
php5-mcrypt \  
php5-gd \  
php5-xdebug \  
php5-curl  
  
# Data startup script  
ADD config/data-start.sh /opt/bin/data-start.sh  
ADD config/notice.txt /opt/etc/data-notice.txt  
RUN chmod u=rwx /opt/bin/data-start.sh  
  
ENTRYPOINT ["/opt/bin/data-start.sh"]

