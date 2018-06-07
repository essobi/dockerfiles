FROM debian:sid  
  
MAINTAINER Pavan Kumar <k.pavan@invizotechnologies.com>  
  
# Using debian jessie packages instead of compiling from scratch  
RUN DEBIAN_FRONTEND=noninteractive \  
echo "APT::Install-Recommends \"0\";" >> /etc/apt/apt.conf.d/02recommends && \  
echo "APT::Install-Suggests \"0\";" >> /etc/apt/apt.conf.d/02recommends && \  
apt-get clean && \  
apt-get -q -y update && \  
apt-get -q -y install \  
ca-certificates php5-cli php5-fpm php5-gd libapache2-mod-php5 php5-mysql
php5-curl php5-pgsql php5-sqlite php5-mcrypt \  
wget sqlite git libsqlite3-dev curl supervisor cron unzip software-properties-
common && \  
apt-get clean && apt-get autoremove -q && \  
rm -rf /var/lib/apt/lists/* /usr/share/doc /usr/share/man /tmp/*  
  
# Intall node  
RUN curl -sL https://deb.nodesource.com/setup | bash -  
RUN apt-get -q -y install nodejs npm nodejs-legacy  
  
# Install redis server  
RUN add-apt-repository -y ppa:chris-lea/redis-server && \  
apt-get update && \  
apt-get -q -y install redis-server  
  
# Install Nginx server  
RUN add-apt-repository -y ppa:nginx/stable && apt-get update && apt-get
install -y nginx  
  
COPY configs/supervisord.conf /etc/supervisor/supervisord.conf  
  
RUN sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php5/fpm/php-
fpm.conf && \  
mkdir /run/php  
  
WORKDIR /var/www/deployer/  
  
# Install composer  
RUN curl -sS https://getcomposer.org/installer | php  
  
RUN wget https://github.com/REBELinBLUE/deployer/archive/0.0.33.tar.gz && \  
tar xzvf 0.0.33.tar.gz --strip-components=1 && \  
chown -R www-data /var/www/deployer && \  
rm -r 0.0.33.tar.gz && \  
php composer.phar install --no-dev -o && \  
npm install --production  
  
RUN cp examples/supervisor.conf /etc/supervisor/conf.d/deployer.conf  
RUN cp examples/crontab /etc/cron.d/artisan-schedule  
  
COPY configs/entrypoint.sh /sbin/entrypoint.sh  
RUN chmod +x /sbin/entrypoint.sh  
COPY configs/.env.docker /var/www/deployer/.env  
COPY configs/nginx-site.conf /etc/nginx/sites-available/default  
  
RUN chmod 0644 /etc/cron.d/artisan-schedule &&\  
touch /var/log/cron.log &&\  
chown www-data /var/www/deployer/.env  
  
CMD ["/sbin/entrypoint.sh"]  

