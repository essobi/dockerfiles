FROM webdevops/php-nginx:ubuntu-14.04  
#FROM webdevops/php-nginx:ubuntu-16.04  
COPY nginx_geoip_params /etc/nginx/geoip_params  
COPY nginx_log_format.conf
/opt/docker/etc/nginx/conf.d/10-nginx_log_format.conf  
COPY nginx_real_ip.conf /opt/docker/etc/nginx/conf.d/10-nginx_real_ip.conf  
  
# nginx vhosts config  
COPY vhost.conf /opt/docker/etc/nginx/vhost.conf  
COPY _main-location-ip-rules.conf /opt/docker/etc/nginx/_main-location-ip-
rules.conf  
COPY _more.conf /opt/docker/etc/nginx/_more.conf  
COPY _http-basic-auth.conf /opt/docker/etc/nginx/_http-basic-auth.conf  
COPY _htpasswd /opt/docker/etc/nginx/_htpasswd  
  
COPY entry.sh /entry.sh  
  
RUN mkdir -p /usr/share/GeoIP  
RUN wget -q -O-
http://geolite.maxmind.com/download/geoip/database/GeoLiteCountry/GeoIP.dat.gz
| gunzip > /usr/share/GeoIP/GeoIP.dat  
RUN wget -q -O-
http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz | gunzip
> /usr/share/GeoIP/GeoLiteCity.dat  
  
RUN apt-get update  
  
RUN mkdir -p /var/log/php5-fpm/  
  
#RUN apt-get -q -y install php5-mongo  
#RUN apt-get -q -y install php7-mongo # this line is for basing on
ubuntu-16.04  
#ref: http://www.bictor.com/2015/02/15/installing-mongodb-for-php-in-
ubuntu-14-04/  
#ref: https://github.com/mongodb/mongo-php-driver/issues/138  
#ref: http://stackoverflow.com/questions/22555561/error-building-fatal-error-
pcre-h-no-such-file-or-directory  
#ref: https://docs.mongodb.com/ecosystem/drivers/php/  
RUN apt-get -q -y install php-pear php5-dev  
RUN apt-get -q -y install libcurl4-openssl-dev pkg-config libssl-dev
libsslcommon2-dev  
RUN apt-get -q -y install libpcre3-dev  
  
RUN pecl install mongodb  
RUN echo "extension=mongodb.so" | sudo tee /etc/php5/mods-
available/mongodb.ini  
RUN sudo ln -sfn ../../mods-available/mongodb.ini
/etc/php5/cli/conf.d/20-mongodb.ini  
RUN sudo ln -sfn ../../mods-available/mongodb.ini
/etc/php5/fpm/conf.d/20-mongodb.ini  
  
RUN pecl install mongo  
RUN echo "extension=mongo.so" | sudo tee /etc/php5/mods-available/mongo.ini  
RUN sudo ln -sfn ../../mods-available/mongo.ini
/etc/php5/cli/conf.d/20-mongo.ini  
RUN sudo ln -sfn ../../mods-available/mongo.ini
/etc/php5/fpm/conf.d/20-mongo.ini  
  
# do not use native mysql driver  
RUN sudo apt-get -q -y remove php5-mysqlnd  
RUN sudo apt-get -q -y install php5-mysql  
  
RUN sudo apt-get -q -y install php5-gmp  
  
CMD ["/entry.sh"]  

