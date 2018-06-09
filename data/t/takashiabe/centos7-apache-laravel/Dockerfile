FROM takashiabe/centos7-apache-php  
  
RUN curl -sL https://rpm.nodesource.com/setup_8.x | bash -  
RUN yum -y update && yum -y install nodejs gcc gcc-c++ make openssl-devel
libpng libpng-devel autogen libtool wget nasm && yum clean all && rm -rf
/var/cache/yum  
  
RUN mkdir /var/www_tmp && cd /var/www_tmp && composer create-project
"laravel/laravel=5.6.*" \--prefer-dist laravel  
  
RUN cd /var/www_tmp/laravel && composer require "laravel-ja/comja5:~1"  
COPY ./gulpfile.js /var/www_tmp/laravel/  
RUN cd /var/www_tmp/laravel && ./vendor/bin/comja5 -c  
  
COPY ./docker-entrypoint.sh /  
  
RUN chmod +x /docker-entrypoint.sh  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
EXPOSE 80  
CMD ["/usr/sbin/init"]  
  

