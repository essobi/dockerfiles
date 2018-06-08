FROM ubuntu  
RUN apt-get update  
RUN apt-get -y install git nginx nginx-extras php5-dev php5-fpm php5-curl
php5-mysql php5-mcrypt libpcre3-dev gcc make && \  
mkdir /var/www && \  
/usr/bin/git clone https://github.com/phalcon/cphalcon.git && \  
cd cphalcon/build/ && \  
./install && \  
cd /tmp && \  
/bin/rm -rf /tmp/cphalcon/ && \  
/usr/bin/apt-get -y purge git php5-dev libpcre3-dev gcc make && apt-get -y
autoremove && apt-get clean && \  
echo 'extension=phalcon.so' >> /etc/php5/fpm/conf.d/30-phalcon.ini && \  
echo 'extension=phalcon.so' >> /etc/php5/cli/conf.d/30-phalcon.ini && \  
cp /etc/php5/mods-available/mcrypt.ini /etc/php5/fpm/conf.d/20-mcrypt.ini  
  
ADD nginx.conf /etc/nginx/nginx.conf  
ADD default /etc/nginx/sites-available/default  
ADD default-ssl /etc/nginx/sites-enabled/default-ssl  
  
ADD server.crt /etc/nginx/ssl/  
ADD server.key /etc/nginx/ssl/  
  
EXPOSE 80  
CMD service php5-fpm start && nginx

