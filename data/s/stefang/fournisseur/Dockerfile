FROM ubuntu  
  
MAINTAINER Stefan Gotkowski  
  
ENV DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get update  
  
RUN apt-get install -y \  
git \  
nano \  
php7.0 \  
php7.0-fpm \  
php7.0-mysql \  
nginx \  
openssl  
  
RUN git clone https://github.com/certbot/certbot /opt/letsencrypt && \  
./opt/letsencrypt/certbot-auto --non-interactive --os-packages-only  
  
ADD index.php /var/www/html/index.php  
ADD scriptFournisseur.sh /script.sh  
ADD renew-letsencrypt.sh /renew-letsencrypt.sh  
RUN chmod +x /script.sh && rm /var/www/html/*.html  
  
EXPOSE 80 443  

