# guanxiaohua2k6/centos-apache-php  
#  
# centos7, apache 2.4, php 5.6, git, drupal  
FROM centos:7  
MAINTAINER Xiaohua Guan <guan@ipride.co.jp>  
  
#install php & httpd  
RUN yum -y install http://rpms.famillecollet.com/enterprise/remi-release-7.rpm  
RUN yum -y install --enablerepo=remi,remi-php56 php php-opcache php-devel php-
mbstring php-mcrypt php-mysqlnd php-pecl-xdebug php-pecl-xhprof php-gd php-fpm
php-twig-ctwig httpd  
  
RUN php -v  
  
#install ssl  
RUN yum -y install openssl mod_ssl  
  
#install git  
RUN yum -y install git  
RUN git --version  
  
#composer  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/bin/composer  
#RUN composer global require drush/drush:dev-master  
#drupal  
RUN composer global require drupal/console:dev-master  
ENV PATH /root/.composer/vendor/bin:$PATH  
RUN echo $PATH  
RUN drupal --version  
  
#update httpd.conf  
ADD httpd.conf /etc/httpd/conf/httpd.conf  
RUN cat /etc/httpd/conf.d/ssl.conf  
  
#update php.ini  
ADD php.ini /etc/php.ini  
  
#port and entry  
EXPOSE 80  
#EXPOSE 443  
CMD ["/usr/sbin/httpd", "-D", "FOREGROUND"]  

