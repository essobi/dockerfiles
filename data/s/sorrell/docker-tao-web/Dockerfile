FROM php:7.0.5-apache  
  
MAINTAINER Nick Sorrell <nick@cint.io>  
  
ARG TAO_SERVER_NAME  
ENV TAO_SERVER_NAME=$TAO_SERVER_NAME  
  
RUN export DEBIAN_FRONTEND=noninteractive  
ENV DEBIAN_FRONTEND noninteractive  
RUN dpkg-divert --local \--rename --add /sbin/initctl  
  
# Use local cached debs from host (saves your bandwidth!)  
# Change ip below to that of your apt-cacher-ng host  
# Or comment this line out if you do not wish to use caching  
ADD 71-apt-cacher-ng /etc/apt/apt.conf.d/71-apt-cacher-ng  
  
RUN apt-get -y update && \  
apt-get install -y \  
curl \  
libcurl4-gnutls-dev \  
libpng-dev \  
libpq-dev \  
libxml2-dev \  
libtidy-dev \  
unzip \  
mc  
  
RUN docker-php-ext-install -j$(nproc) \  
curl \  
gd \  
pdo_pgsql \  
zip \  
tidy \  
xml  
  
RUN a2enmod rewrite  
  
ADD http://releases.taotesting.com/TAO_3.1.0-RC7_build.zip
/tmp/TAO_3.1.0-RC7_build.zip  
ADD https://github.com/mathjax/MathJax/archive/2.7.0.zip /tmp/2.7.0.zip  
  
WORKDIR /tmp  
  
RUN unzip -q TAO_3.1.0-RC7_build.zip; \  
mv TAO_3.1.0-RC7_build web; \  
mv web /home/; \  
unzip -q 2.7.0.zip; \  
mv MathJax-2.7.0/* /home/web/taoQtiItem/views/js/mathjax/; \  
chown -R www-data.www-data /home/web  
  
ADD apache.conf /etc/apache2/sites-enabled/000-default.conf  
RUN sed -i -e "s/TAO_SERVER_NAME/${TAO_SERVER_NAME}/g" /etc/apache2/sites-
enabled/000-default.conf  
  
ADD php.ini /usr/local/etc/php/  
  
EXPOSE 80  
CMD ["/usr/sbin/apachectl", "-D", "FOREGROUND"]  

