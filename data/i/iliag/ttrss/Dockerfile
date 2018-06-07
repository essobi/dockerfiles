FROM phusion/baseimage:latest  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update \  
&& apt-get install -y wget \  
&& apt-get install -y htop nginx php5-fpm php5-cli php5-gd php5-mysql
php5-curl php5-mcrypt \--no-install-recommends \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN mkdir /home/vhosts \  
&& cd /home/vhosts \  
&& wget https://tt-rss.org/gitlab/fox/tt-rss/repository/archive.tar?ref=master
-O ttrss.tar \  
&& tar -xf ttrss.tar \  
&& mv /home/vhosts/tt-rss.git /home/vhosts/ttrss \  
&& rm -f ttrss.tar \  
&& rm -f /etc/nginx/sites-enabled/default \  
&& echo "extension=mcrypt.so" > /etc/php5/cli/conf.d/20-mcrypt.ini \  
&& echo "extension=mcrypt.so" > /etc/php5/fpm/conf.d/20-mcrypt.ini \  
&& mkdir /home/vhosts/ttrss/cache2 \  
&& cp -nR /home/vhosts/ttrss/cache/* /home/vhosts/ttrss/cache2/ \  
&& chown -R www-data:www-data /home/vhosts/ttrss \  
&& chmod -R 777 /home/vhosts/ttrss  
  
  
COPY etc /etc  
  
EXPOSE 80  
  
CMD ["/sbin/my_init"]  

