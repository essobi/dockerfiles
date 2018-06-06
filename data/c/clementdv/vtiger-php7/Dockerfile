FROM debian:latest  
  
# install the PHP extensions we need  
RUN apt update && apt upgrade -y && apt install -y php7.0 apache2
libapache2-mod-php7.0 php-imap php-curl php-xml curl  
  
ENV DB_HOSTNAME="mysql"  
ENV DB_USERNAME="root"  
ENV DB_PASSWORD="rootpassword"  
ENV DB_NAME="vtiger"  
WORKDIR /var/www/html  
  
RUN rm index.html \  
&& curl -o vtigercrm.tar.gz -SL
https://sourceforge.net/projects/vtigercrm/files/vtiger%20CRM%207.1.0/Core%20Product/vtigercrm7.1.0.tar.gz/
\  
&& tar -xzf vtigercrm.tar.gz --strip-components=1 \  
&& rm vtigercrm.tar.gz \  
&& chmod -R 775 ../html \  
&& service apache2 restart  
  
COPY docker-entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["apache2 -DFOREGROUND"]  

