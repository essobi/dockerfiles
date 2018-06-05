FROM php:5.6-apache  
  
LABEL "MAINTAINER"="Sakarin Kammanee <Sakarin@coe.phuket.psu.ac.th>"  
  
ENV TZ=Asia/Bangkok  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  
  
RUN apt-get update && apt-get install -y \  
git  
  
RUN docker-php-ext-install mbstring  
  
RUN git clone https://github.com/ptrofimov/beanstalk_console.git
/tmp/beanstalk_console  
  
RUN cp -r /tmp/beanstalk_console/public /var/www/ && \  
cp -r /tmp/beanstalk_console/lib /var/www/ && \  
cp -r /tmp/beanstalk_console/config.php /var/www && \  
cp -r /tmp/beanstalk_console/src /var/www && \  
cp /tmp/beanstalk_console/docker/apache_default /etc/apache2/apache2.conf && \  
cp /tmp/beanstalk_console/docker/run.sh /usr/local/bin/run && \  
cp /tmp/beanstalk_console/docker/php.ini /usr/local/lib/php.ini && \  
cp /tmp/beanstalk_console/LICENSE.md /var/www && \  
chown -R www-data:www-data /var/www && \  
chmod +x /usr/local/bin/run && \  
a2enmod rewrite && \  
a2dissite 000-default  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
WORKDIR /var/www  
CMD ["/usr/local/bin/run"]  

