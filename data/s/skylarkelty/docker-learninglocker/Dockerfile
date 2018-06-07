FROM skylarkelty/centos:latest  
MAINTAINER "Skylar Kelty" <s.kelty@kent.ac.uk>  
ADD ./shared/files/remi.repo /etc/yum.repos.d/remi.repo  
ADD ./shared/files/nginx.repo /etc/yum.repos.d/nginx.repo  
RUN yum install -y http://rpms.remirepo.net/enterprise/remi-release-7.rpm \  
nginx cronie \  
&& yum clean all  
RUN yum-config-manager --enable remi-php56 && \  
yum install -y php56 php56-php-fpm php56-php-opcache php56-php-cli \  
php56-php-gd php56-php-pdo php56-php-xml php56-php-intl php56-php-pear \  
php56-php-soap php56-php-xmlrpc php56-php-process php56-php-mysqlnd \  
php56-php-mbstring php56-php-ldap php56-php-mcrypt php56-php-mssql \  
php56-php-pecl-memcache php56-php-pecl-memcached php56-php-pecl-solr2 \  
php56-php-pecl-mongodb php56-php-pecl-mongo php56-php-pecl-redis php56-php-
pecl-zip \  
&& yum clean all  
RUN ln -s /usr/bin/php56 /usr/bin/php && \  
ln -s /usr/bin/php56-cgi /usr/bin/php-cgi && \  
ln -s /usr/bin/php56-pear /usr/bin/php-pear && \  
ln -s /usr/bin/php56-phar /usr/bin/php-phar  
ADD ./shared/puppet /puppet  
RUN yum install -y puppet && \  
puppet apply --modulepath=/puppet/modules /puppet/manifests/site.pp && \  
yum remove -y puppet && yum clean all  
RUN date > /etc/docker-release  
  
EXPOSE 22 80 443  
CMD ["/usr/sbin/init"]  

