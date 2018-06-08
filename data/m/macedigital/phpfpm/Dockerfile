FROM centos:7  
MAINTAINER Matthias Adler <macedigital@gmail.com>  
  
RUN yum install -y epel-release https://mirror.webtatic.com/yum/el7/webtatic-
release.rpm \  
&& yum install -y --enablerepo=webtatic-testing \  
php71w-bcmath \  
php71w-fpm \  
php71w-gd \  
php71w-imap \  
php71w-intl \  
php71w-ldap \  
php71w-mbstring \  
php71w-mcrypt \  
php71w-mysqlnd \  
php71w-opcache \  
php71w-pdo \  
php71w-pecl-apcu \  
php71w-pecl-imagick \  
php71w-pgsql \  
php71w-process \  
php71w-recode \  
php71w-soap \  
php71w-xml \  
&& yum clean all  
  
COPY php-fpm.conf /etc/php-fpm.conf  
COPY www.conf /etc/php-fpm.d/www.conf  
  
RUN mkdir -p /var/lib/php/{session,wsdlcache} && chown -R apache:apache
/var/lib/php  
  
EXPOSE 9000  
VOLUME [ "/var/www" ]  
  
CMD ["php-fpm", "-F", "-O"]  

