FROM skylarkelty/centos:latest  
MAINTAINER "Skylar Kelty" <s.kelty@kent.ac.uk>  
ADD ./shared/files/remi.repo /etc/yum.repos.d/remi.repo  
ADD ./shared/files/nginx.repo /etc/yum.repos.d/nginx.repo  
ADD ./shared/files/supervisord.service /etc/systemd/system/multi-
user.target.wants/supervisord.service  
RUN yum install -y http://rpms.remirepo.net/enterprise/remi-release-7.rpm \  
nginx cronie python-setuptools \  
&& yum clean all  
RUN easy_install supervisor  
RUN yum-config-manager --enable remi-php70 && \  
yum install -y php70 php70-php-fpm php70-php-opcache php70-php-cli \  
php70-php-gd php70-php-pdo php70-php-xml php70-php-intl php70-php-pear \  
php70-php-soap php70-php-xmlrpc php70-php-process php70-php-mysqlnd \  
php70-php-mbstring php70-php-ldap php70-php-mcrypt \  
php70-php-pecl-memcache php70-php-pecl-memcached php70-php-pecl-zip && yum
clean all  
RUN ln -s /usr/bin/php70 /usr/bin/php && \  
ln -s /usr/bin/php70-cgi /usr/bin/php-cgi && \  
ln -s /usr/bin/php70-pear /usr/bin/php-pear && \  
ln -s /usr/bin/php70-phar /usr/bin/php-phar  
ADD ./shared/simplesamlphp /var/www/vhosts/myfolio-
dev.kent.ac.uk/sp/simplesamlphp  
ADD ./shared/puppet /puppet  
RUN yum install -y puppet && \  
puppet apply --modulepath=/puppet/modules /puppet/manifests/site.pp && \  
yum remove -y puppet && yum clean all  
RUN date > /etc/docker-release  
  
EXPOSE 22 80 443  
CMD ["/usr/sbin/init"]  

