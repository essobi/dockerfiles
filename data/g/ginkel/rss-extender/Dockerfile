FROM tgbyte/nginx-php-fpm  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y git &&
\  
git clone --depth 1 https://github.com/ginkel/rss-extender.git /var/www && \  
rm -rf /var/www/.git && \  
mkdir /var/www/tmp && \  
chown www-data.www-data /var/www/tmp && \  
apt-get remove -y --purge git && \  
apt-get autoremove -y --purge && \  
apt-get clean && rm -rf /var/lib/apt/lists/*  
  
ADD rss-extender.nginx.conf /etc/nginx/conf.d/rss-extender.conf  
VOLUME /var/www/tmp  
WORKDIR /var/www/tmp  

