From romeohua/simple-php7:pubroot  
  
ENV BASEDIR /  
  
RUN yum -y update && yum install -y git sudo && yum clean all  
  
# Edit sudoers file  
# To avoid error: sudo: sorry, you must have a tty to run sudo  
RUN sed -i -e "s/Defaults requiretty.*/ #Defaults requiretty/g" /etc/sudoers  
  
WORKDIR ${BASEDIR}  
  
RUN git clone \--depth=1 https://github.com/ice/framework.git  
RUN git clone \--depth=1 -b php7 https://github.com/phpredis/phpredis.git  
  
WORKDIR /framework  
RUN export PATH=$PATH:/usr/local/php/bin && ./install  
  
#RUN echo "extension=/framework/build/php7/modules/ice.so" >>
/usr/local/php/etc/php.d/ice.ini  
ADD ice.ini /usr/local/php/etc/php.d/ice.ini  
  
WORKDIR /phpredis  
RUN export PATH=$PATH:/usr/local/php/bin && phpize && ./configure && make &&
make install  
ADD phpredis.ini /usr/local/php/etc/php.d/phpredis.ini  
  
# Install phpunit  
RUN wget https://phar.phpunit.de/phpunit.phar && chmod +x phpunit.phar && mv
phpunit.phar /usr/local/bin/phpunit  
  
RUN supervisorctl restart nginx  
  
RUN supervisorctl restart php-fpm

