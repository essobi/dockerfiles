FROM nginx:alpine  
MAINTAINER Enrico204 <enrico204@gmail.com>  
  
ENV FRIENDICA_VERSION 3.5.2  
ENV ADDONS_VERSION 3.5.2  
RUN apk update && apk add php5-mysqli php5-fpm git curl php5-gd php5-mcrypt
php5-xml php5-iconv php5-openssl php5-dom dcron php5-curl \  
php5-imagick openssl php5-json php5-ctype php5-posix && \  
rm /usr/share/nginx/html/*  
RUN git clone https://github.com/friendica/friendica.git
/usr/share/nginx/html/ && rm /usr/share/nginx/html/.git* -rf  
RUN git clone https://github.com/friendica/friendica-addons.git
/usr/share/nginx/html/addon/ && rm /usr/share/nginx/html/addon/.git* -rf  
RUN apk del git && chmod a+w /usr/share/nginx/html/view/smarty3/ && \  
touch /usr/share/nginx/html/.htconfig.php && chmod a+w
/usr/share/nginx/html/.htconfig.php  
RUN echo "*/10 * * * * cd /usr/share/nginx/html/; /usr/bin/php
include/poller.php" >> /etc/crontabs/root  
  
COPY friendica.conf /etc/nginx/conf.d/default.conf  
COPY start.sh /opt/start.sh  
  
EXPOSE 80  
CMD [ "/bin/sh", "/opt/start.sh" ]  

