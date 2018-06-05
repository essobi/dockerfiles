FROM centos:6  
MAINTAINER Marijn Giesen <marijn@studio-donder.nl>  
  
# Install repositories, update system and install software  
RUN yum -y install \--setopt=tsflags=nodocs
http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm \  
http://rpms.famillecollet.com/enterprise/remi-release-6.rpm \  
http://sphinxsearch.com/files/sphinx-2.2.9-1.rhel6.x86_64.rpm && \  
sed -i -e '/\\[remi\\]/,/^\\[/s/enabled=0/enabled=1/'
/etc/yum.repos.d/remi.repo; \  
yum -y update \--setopt=tsflags=nodocs; \  
yum -y \--setopt=tsflags=nodocs install php-fpm php php-bcmath php-mysql php-
common php-pdo php-mbstring php-pecl-redis \  
php-gd php-xml php-mcrypt php-soap php-pecl-imagick php-pecl-apc php-pecl-
oauth php-pecl-igbinary php-pecl-memcached \  
php-cli php-pear python-pip redis memcached ImageMagick GraphicsMagick
phpMyAdmin nodejs npm libpng-devel cairo-devel \  
freetype-devel libjpeg-turbo-devel which tar bzip2 gcc make autoconf automake
libtool php-xdebug git; \  
rm -rf /var/cache/yum/*; \  
yum clean all  
  
# Configure software  
RUN pip install pip \--upgrade && pip install setuptools \--upgrade && pip
install supervisor; \  
npm install -g grunt && npm install -g grunt-cli; \  
echo "NETWORKING=yes" > /etc/sysconfig/network; \  
rm -rf /tmp/*; \  
mkdir -p /data/{bootstrap,db,www,log}; mkdir -p /etc/service-config; \  
sed -i 's/^\(bind .*\\)$/# \1/' /etc/redis.conf && \  
sed -i 's/^\(daemonize .*\\)$/# \1/' /etc/redis.conf && \  
sed -i 's/^dir .*$/dir \/data\/db\/redis/' /etc/redis.conf && \  
sed -i 's/^logfile .*$/logfile \/data\/log\/redis\/redis.log/' /etc/redis.conf  
  
COPY etc/service-config /etc/service-config  
COPY bootstrap/start_container /usr/bin/start_container  
  
RUN ln -sf /etc/service-config/supervisor/supervisord.conf
/etc/supervisord.conf && \  
ln -sf /etc/service-config/php/www.conf /etc/php-fpm.d/www.conf && \  
ln -sf /etc/service-config/php/php.ini /etc/php.ini && \  
ln -sf /etc/service-config/php/php-fpm.conf /etc/php-fpm.conf; \  
ln -sf /usr/share/zoneinfo/Europe/Amsterdam /etc/localtime; \  
chmod 700 /usr/bin/start_container  
  
EXPOSE 6379 9306 11211  
  
CMD ["/usr/bin/start_container", "app"]  

