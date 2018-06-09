FROM mba811/nginx-php:latest  
MAINTAINER Tsong khapa <ztd811@yahoo.com>  
CMD /bin/sh -c apt-get install -y git && \  
apt-get clean && \  
echo -n > /var/lib/apt/extended_states  
ADD config /config  
ADD supervisord.conf /etc/supervisor/conf.d/tiny-tiny-rss.conf

