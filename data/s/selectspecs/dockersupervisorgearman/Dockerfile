FROM ubuntu-debootstrap  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN BUILD_PACKAGES="supervisor wget libboost-all-dev gperf build-essential
libevent-dev uuid-dev gearman-job-server python-pip gearman-job-server
php5-fpm git php5-mysql php5-dev libcurl4-openssl-dev php5-curl php5-gd
php5-intl php5-mcrypt php5-memcache php5-sqlite php5-tidy php5-xmlrpc php5-xsl
php5-mysql php5-gd php5-imagick php5-imap php5-sqlite php5-xsl php5-pgsql
php5-mongo php-pear libgearman-dev libcurl4-openssl-dev libxml2-dev
libpcre3-dev" && \  
apt-get update && \  
apt-get -y install --no-install-recommends $BUILD_PACKAGES && \  
pip install supervisor-stdout  
  
RUN echo "\n\n\n\n\n\n\n\n\n" | pecl install gearman && \  
echo "extension=gearman.so" > /etc/php5/mods-available/gearman.ini && \  
php5enmod gearman && \  
pear install Net_Gearman channel://pear.php.net/Net_Gearman-0.2.3  
  
RUN apt-get autoremove -y && \  
apt-get clean && \  
apt-get autoclean && \  
rm -rf /var/lib/apt/lists/*  
RUN useradd -ms /bin/bash worker  
# Supervisor Config  
ADD ./supervisord.conf /etc/supervisor/supervisord.conf  
RUN mkdir -p /var/log/gearman  
# Start Supervisord  
ADD ./start.sh /start.sh  
RUN chmod 755 /start.sh  
  
CMD ["/bin/bash", "/start.sh"]  
  

