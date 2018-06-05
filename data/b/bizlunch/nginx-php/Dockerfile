FROM bizlunch/nginx  
  
RUN DEBIAN_FRONTEND=noninteractive add-apt-repository ppa:ondrej/php --yes  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \  
php7.1-cli php7.1-fpm php7.1-curl php7.1-zip php7.1-pdo php7.1-gd php7.1-xml
php7.1-apcu php7.1-mysql php7.1-intl \  
git  
  
ADD services/php /etc/service/php/run  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
RUN chmod +x /etc/service/php/run && \  
mkdir -p /opt/bizlunch/cache /var/lib/php/session && \  
chown www-data:www-data -R /opt/bizlunch /var/lib/php/session && \  
rm -rf /var/lib/apt/lists/*  

