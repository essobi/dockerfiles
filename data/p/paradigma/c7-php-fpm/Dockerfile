FROM centos:centos7  
MAINTAINER Greco Rubio <greco@paradigma.com.mx>  
  
RUN yum -y update; yum clean all  
RUN yum -y install epel-release tar ; yum clean all  
RUN yum -y install php php-fpm php-common ; yum clean all  
RUN yum -y install php-pecl-apc php-cli php-pear php-pdo php-pgsql \  
php-pecl-mongo php-pecl-memcache php-pecl-memcached php-gd php-mbstring \  
php-mcrypt php-xml php-mysqlnd php-zip php-iconv php-curl php-simplexml \  
php-dom php-bcmath php-opcache ; yum clean all  
  
RUN groupadd www-data ; useradd -g www-data www-data  
  
RUN mv /etc/php-fpm.conf /etc/php-fpm.conf.default  
ADD php-fpm.conf /etc/php-fpm.conf  
RUN mv /etc/php.ini /etc/php.ini.default  
ADD php.ini /etc/php.ini  
RUN echo "cgi.fix_pathinfo = 0;" >> /etc/php.ini  
RUN mv /etc/php-fpm.d/www.conf /etc/php-fpm.d/www.conf.default  
ADD www.conf /etc/php-fpm.d/www.conf  
  
RUN mkdir -p /etc/service/php5fpm  
ADD start.sh /etc/service/php5fpm/run  
RUN chmod +x /etc/service/php5fpm/run  
  
EXPOSE 9000  
ENTRYPOINT ["/etc/service/php5fpm/run"]  
  
CMD ["start"]

