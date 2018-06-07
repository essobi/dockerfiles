FROM php:7-fpm  
  
MAINTAINER jerome.bernard@gmail.com  
  
ENV SHELL_ROOT_PASSWORD Mjeedom96  
  
RUN apt-get update && apt-get install -y \  
apt-utils \  
wget \  
libssh2-php \  
ntp \  
unzip \  
curl \  
openssh-server \  
supervisor \  
cron \  
usb-modeswitch \  
python-serial \  
nodejs \  
npm \  
tar \  
libmcrypt-dev \  
libcurl4-gnutls-dev \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libpng12-dev \  
libxml2-dev \  
sudo \  
htop \  
net-tools \  
python \  
ca-certificates \  
vim \  
git \  
g++ \  
locate \  
mysql-client \  
telnet \  
man \  
usbutils \  
libtinyxml-dev \  
libjsoncpp-dev \  
snmp \  
libsnmp-dev \  
iputils-ping \  
nginx-common \  
nginx-full  
  
  
  
################################################################### PHP7
##########################################  
  
RUN docker-php-ext-install json  
RUN docker-php-ext-install mcrypt  
RUN docker-php-ext-install curl  
RUN docker-php-ext-install opcache  
RUN docker-php-ext-install pdo  
RUN docker-php-ext-install pdo_mysql  
RUN docker-php-ext-install posix  
RUN docker-php-ext-install simplexml  
RUN docker-php-ext-install sockets  
RUN docker-php-ext-install zip  
RUN docker-php-ext-install iconv  
RUN docker-php-ext-install mbstring  
RUN docker-php-ext-install mysqli  
RUN docker-php-ext-install soap  
RUN docker-php-ext-install snmp  
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/  
RUN docker-php-ext-install gd  
RUN docker-php-ext-install calendar  
  
RUN rm /usr/bin/php  
RUN ln -s /usr/local/bin/php /usr/bin/php  
RUN echo "max_execution_time = 600" >> /usr/local/etc/php/conf.d/jeedom.ini  
RUN echo "upload_max_filesize = 1G" >> /usr/local/etc/php/conf.d/jeedom.ini  
RUN echo "post_max_size = 1G" >> /usr/local/etc/php/conf.d/jeedom.ini  
RUN echo "expose_php = Off" >> /usr/local/etc/php/conf.d/jeedom.ini  
  
# Install Redis extension for PHP  
RUN pecl install -o -f redis \  
&& rm -rf /tmp/pear \  
&& echo "extension=redis.so" > /usr/local/etc/php/conf.d/redis.ini  
  
  
################################################################### JEEDOM
########################################  
  
RUN mkdir -p /var/www/html  
RUN rm -rf /root/core-*  
RUN wget https://github.com/jeedom/core/archive/stable.zip -O /tmp/jeedom.zip  
RUN unzip -q /tmp/jeedom.zip -d /root/  
RUN cp -R /root/core-*/* /var/www/html/  
RUN cp -R /root/core-*/.htaccess /var/www/html/  
RUN chown -R www-data:www-data /var/www/html  
  
  
################################################################### NGINX
#########################################  
  
RUN mkdir -p /var/www/html/log  
RUN rm /etc/nginx/sites-available/default  
RUN rm /etc/nginx/sites-enabled/default  
RUN wget
https://raw.githubusercontent.com/jeedom/core/stable/install/nginx_default -O
/etc/nginx/sites-available/default  
RUN ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default  
RUN touch /etc/nginx/sites-available/jeedom_dynamic_rule  
RUN ln -s /etc/nginx/sites-available/jeedom_dynamic_rule /etc/nginx/sites-
enabled/jeedom_dynamic_rule  
RUN sed -i 's/usr\/share\/nginx\/www\/jeedom/var\/www\/html/g'
/etc/nginx/sites-enabled/default  
RUN sed -i 's/unix:\/var\/run\/php5-fpm.sock/localhost:9000/g'
/etc/nginx/sites-enabled/default  
  
################################################################### SYSTEM
########################################  
  
RUN echo "root:${SHELL_ROOT_PASSWORD}" | chpasswd && \  
sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config && \  
sed -i 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' /etc/pam.d/sshd  
  
RUN echo "* * * * * su --shell=/bin/bash - www-data -c '/usr/bin/php
/var/www/html/core/php/jeeCron.php' >> /dev/null" | crontab -  
  
RUN echo "www-data ALL=(ALL) NOPASSWD: ALL" | (EDITOR="tee -a" visudo)  
  
RUN mkdir -p /var/run/sshd /var/log/supervisor  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
ADD init.sh /root/init.sh  
RUN chmod +x /root/init.sh  
RUN mkdir -p /tmp/jeedom-cache  
RUN chown -R www-data:www-data /tmp/jeedom-cache  
  
################################################################### MQTT
##########################################  
  
RUN wget http://repo.mosquitto.org/debian/mosquitto-repo.gpg.key  
RUN apt-key add mosquitto-repo.gpg.key  
# cd /etc/apt/sources.list.d/  
# if [ `lsb_release -c -s` == "jessie" ]; then  
# wget http://repo.mosquitto.org/debian/mosquitto-jessie.list  
# rm /etc/apt/sources.list.d/mosquitto-jessie.list  
# cp -r mosquitto-jessie.list /etc/apt/sources.list.d/mosquitto-jessie.list  
# fi  
  
RUN apt-get update && apt-get install -y \  
mosquitto mosquitto-clients libmosquitto-dev \  
php5-dev  
  
WORKDIR /tmp  
RUN git clone https://github.com/mgdm/Mosquitto-PHP.git  
WORKDIR /tmp/Mosquitto-PHP  
RUN phpize  
RUN ./configure --with-mosquitto=/usr/lib  
RUN make  
RUN make install  
WORKDIR /var/www/html  
  
################################################################### START
########################################  
  
CMD ["/root/init.sh"]  
  
EXPOSE 22 80 162 1886 4025 17100 10000  
  
#17100 : zibasdom  
#10000 : orvibo  
#1886 : MQTT  
#162 : SNMP  
#4025 : DSC  

