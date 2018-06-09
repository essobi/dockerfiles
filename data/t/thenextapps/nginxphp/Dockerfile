FROM phusion/baseimage:0.9.19  
MAINTAINER thenextapps@gmail.com  
  
ENV HOME /root  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN /etc/my_init.d/00_regen_ssh_host_keys.sh  
  
# BASIC  
RUN \  
sed -i 's/# \\(.*multiverse$\\)/\1/g' /etc/apt/sources.list && \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y build-essential && \  
apt-get install -y software-properties-common && \  
apt-get install -y byobu curl git htop man unzip vim wget && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# NGINX & PHP  
RUN \  
# nginx and php dependencies  
add-apt-repository -y ppa:nginx/stable && \  
apt-get update -y && \  
apt-get install -yq git curl vim screen htop tree mysql-client-5.7 ant && \  
apt-get install -yq nginx php php-fpm php-mysql php-intl php-gd php-curl php-
apcu php-dev php-cli php7.0-mbstring && \  
# phpunit  
wget https://phar.phpunit.de/phpunit.phar && \  
chmod +x phpunit.phar && \  
mv phpunit.phar /usr/local/bin/phpunit && \  
# git  
apt-get -yq install git-core && \  
git config --global alias.st status && \  
git config --global alias.co checkout && \  
git config --global core.editor vim && \  
git config --global color.ui true  
  
# JS TOOLS  
RUN \  
apt-get -y install nodejs && \  
apt-get -y install npm && \  
ln -s /usr/bin/nodejs /usr/local/bin/node && \  
npm install -g less && \  
npm install -g bower && \  
npm install -g grunt-cli  
  
# PDF CONVERSION  
RUN \  
apt-get update && \  
apt-get install -y xvfb && \  
apt-get install -y libxrender1 xfonts-75dpi fontconfig && \  
wget
http://download.gna.org/wkhtmltopdf/0.12/0.12.2.1/wkhtmltox-0.12.2.1_linux-
trusty-amd64.deb && \  
dpkg -i wkhtmltox-0.12.2.1_linux-trusty-amd64.deb && \  
echo 'exec xvfb-run -a -s "-screen 0 640x480x16" wkhtmltopdf "$@"' | tee
/usr/local/bin/wkhtmltopdf.sh >/dev/null && \  
chmod a+x /usr/local/bin/wkhtmltopdf.sh  
  
# SCRIPTS  
ADD start.sh /tmp/start.sh  
RUN chmod +x /tmp/start.sh  
ADD nginx.conf /etc/nginx/nginx.conf  
RUN rm /etc/nginx/sites-enabled/default  
  
# INSTALL XDEBUG /usr/lib/php7/20121212/  
RUN pecl install xdebug  
ADD xdebug.ini /etc/php/7.0/mods-available/xdebug.ini  
WORKDIR /etc/php/7.0/fpm/conf.d  
RUN ln -s ../../mods-available/xdebug.ini  
WORKDIR /etc/php/7.0/cli/conf.d  
RUN ln -s ../../mods-available/xdebug.ini  
  
# POSTFIX & TELNET  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install postfix  
RUN apt-get -y install telnet  
  
# PHPINI CONFIG  
RUN \  
sed -i 's/max_execution_time = 30/max_execution_time = 300/'
/etc/php/7.0/fpm/php.ini && \  
sed -i 's/memory_limit.*/memory_limit = 1024M/' /etc/php/7.0/fpm/php.ini && \  
sed -i 's/memory_limit.*/memory_limit = 1024M/' /etc/php/7.0/cli/php.ini && \  
#config realpath cache for complex source code  
sed -i 's/\;realpath_cache_size.*/realpath_cache_size = 4096k/'
/etc/php/7.0/fpm/php.ini && \  
sed -i 's/\;realpath_cache_ttl.*/realpath_cache_ttl = 3200/'
/etc/php/7.0/fpm/php.ini && \  
  
sed -i 's/max_execution_time.*/max_execution_time = 600/'
/etc/php/7.0/fpm/php.ini && \  
sed -i 's/max_execution_time.*/max_execution_time = 600/'
/etc/php/7.0/cli/php.ini && \  
  
sed -i 's/\;date\\.timezone\ \=/date\\.timezone\ \=\ \"Australia\/Sydney\"/g'
/etc/php/7.0/fpm/php.ini && \  
sed -i 's/\;date\\.timezone\ \=/date\\.timezone\ \=\ \"Australia\/Sydney\"/g'
/etc/php/7.0/cli/php.ini  
  
# RUN  
CMD /etc/init.d/nginx start && /etc/init.d/php7.0-fpm start && /sbin/my_init  
EXPOSE 80 443 8081 9000 9001 8088  

