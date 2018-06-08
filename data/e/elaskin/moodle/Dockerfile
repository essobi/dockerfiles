FROM ubuntu:16.04  
MAINTAINER elana laskin  
  
COPY moodle-config.php /var/www/html/config.php  
  
# apt-get doesn't allow packages which work in interactive mode. Set all
packages to work in noninteractive mode.  
ENV DEBIAN_FRONTEND noninteractive  
  
# Avoid ERROR: invoke-rc.d: policy-rc.d denied execution of start.  
RUN sed -i "s/^exit 101$/exit 0/" /usr/sbin/policy-rc.d  
  
# to avoid this error: "Automatically disabled Acquire::http::Pipeline-
Depth..."  
RUN echo "Acquire::http::No-Cache true;" >> /etc/apt/apt.conf.d/99mysettings  
RUN echo "Acquire::http::Pipeline-Depth 0;" >>
/etc/apt/apt.conf.d/99mysettings  
  
# add this file which contains additional script commands and make executable  
ADD ./foreground.sh /etc/apache2/foreground.sh  
RUN chmod +x /etc/apache2/foreground.sh  
  
RUN apt-get update && apt-get -y install \  
apt-utils \  
apache2 \  
dnsutils \  
git \  
libapache2-mod-php \  
libssl-dev \  
memcached \  
php \  
php-curl \  
php-intl \  
php-mbstring \  
php-mcrypt \  
php-mysql \  
php-soap \  
php-xml \  
php-xmlrpc \  
php-zip \  
php7.0-gd \  
vim  
  
COPY public_ip.sh .  
COPY localhost.sh .  
RUN chmod +x ./localhost.sh ./public_ip.sh && \  
./localhost.sh  
  
RUN cd /tmp && \  
git clone -b MOODLE_33_STABLE git://git.moodle.org/moodle.git --depth=1  
  
RUN mv /tmp/moodle/* /var/www/html  
RUN rm /var/www/html/index.html  
  
RUN mkdir /var/moodledata  
RUN chown -R www-data /var/moodledata  
RUN chmod -R 777 /var/moodledata  
  
EXPOSE 80  
CMD ["/etc/apache2/foreground.sh"]  

