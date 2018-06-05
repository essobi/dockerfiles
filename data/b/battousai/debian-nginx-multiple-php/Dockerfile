FROM battousai/debian-nginx-multiple:latest  
MAINTAINER Mauro Pinto <mauro.s.pinto@gmail.com>  
  
RUN apt-get update && \  
apt-get install --no-install-recommends -y php5-cli php5-curl php5-fpm php5-gd
php5-mcrypt php5-mysql php5-xdebug && \  
apt-get clean && \  
echo -n > /var/lib/apt/extended_states  
  
RUN rm -rf /etc/nginx/addon.d /etc/php5/fpm/pool.d && \  
mkdir -p /etc/nginx/addon.d /etc/php5/fpm/pool.d  
  
  
ADD etc/php5 /etc/php5  
ADD supervisord.conf /etc/supervisor/conf.d/php-fpm.conf  

