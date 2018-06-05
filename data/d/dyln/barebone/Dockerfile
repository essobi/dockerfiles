FROM phusion/baseimage:0.9.16  
  
# Ensure UTF-8  
RUN locale-gen en_US.UTF-8  
  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
ENV HOME /root  
  
CMD ["/sbin/my_init"]  
  
RUN apt-get update -y && \  
apt-get install -y -o Dpkg::Options::=--force-confnew vim curl wget build-
essential python-software-properties && \  
LC_ALL=C.UTF-8 add-apt-repository -y ppa:nginx/stable && \  
LC_ALL=C.UTF-8 add-apt-repository -y ppa:ondrej/php && \  
apt-get update -y && \  
apt-get install -y -o Dpkg::Options::=--force-confnew nginx php5.6-cli
php5.6-fpm php5.6-curl php5.6-gd php5.6-mcrypt php5.6-intl php5.6-dev php-pear
php5.6-mysql php5.6-xdebug php5.6-sqlite php5.6-xml php5.6-zip php5.6-mongo
php5.6-bcmath php5.6-mbstring && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN sed -i "s/;date.timezone =.*/date.timezone = UTC/"
/etc/php/5.6/fpm/php.ini && \  
sed -i "s/;date.timezone =.*/date.timezone = UTC/" /etc/php/5.6/cli/php.ini &&
\  
echo "daemon off;" >> /etc/nginx/nginx.conf && \  
sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php/5.6/fpm/php-
fpm.conf && \  
touch /var/log/php_errors.log && \  
chmod 777 /var/log/php_errors.log && \  
sed -i "0,/;error_log =.*/s//error_log = \/proc\/self\/fd\/2/"
/etc/php/5.6/fpm/php.ini && \  
sed -i "0,/;error_log =.*/s//error_log = \/proc\/self\/fd\/2/"
/etc/php/5.6/cli/php.ini && \  
usermod -u 1000 www-data && usermod -G staff www-data  
  
ADD xdebug.ini /etc/php/5.6/mods-available/xdebug.ini

