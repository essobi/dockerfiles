FROM idng/basesupervisor  
MAINTAINER IDNG <docker@idng.com>  
  
RUN apt-get update; apt-get upgrade -y -qq; \  
apt-get install -yq wget unzip nginx fontconfig-config fonts-dejavu-core \  
php5-fpm php5-common php5-json php5-cli php5-common php5-mysql\  
php5-gd php5-json php5-mcrypt php5-readline psmisc ssl-cert \  
ufw php-pear libgd-tools libmcrypt-dev mcrypt nano; \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf"]

