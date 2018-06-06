FROM ubuntu:14.04  
MAINTAINER Samuel Okpapi <sokpapi@terragonltd.com>  
  
#RUN echo "deb http://ppa.launchpad.net/kirillshkrogalev/ffmpeg-next/ubuntu
trusty main" > /etc/apt/sources.list  
RUN echo deb http://archive.ubuntu.com/ubuntu precise universe multiverse >>
/etc/apt/sources.list;  
  
#ADD sources.list /etc/apt/  
RUN apt-get update  
# Add the PPA  
RUN apt-get -yqq update  
RUN apt-get -yqq install apache2 git curl php5 libapache2-mod-php5 php5-mcrypt  
  
#VOLUME [ "/var/www/html" ]  
WORKDIR /var/www/html  
  
ADD apache.conf /etc/apache2/sites-available/000-default.conf  
ADD php.conf /etc/php5/apache2/php.ini  
RUN rm -rf /var/www/html/*  
ADD . /var/www/html  
RUN ls -larth /var/www/html  
RUN a2enmod rewrite  
RUN chown -R www-data:www-data /var/www/html  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_PID_FILE /var/run/apache2.pid  
ENV APACHE_RUN_DIR /var/run/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
RUN service apache2 restart  
RUN mkdir -p $APACHE_RUN_DIR $APACHE_LOCK_DIR $APACHE_LOG_DIR  
  
EXPOSE 80  
ENTRYPOINT [ "/usr/sbin/apache2" ]  
CMD ["-D", "FOREGROUND"]

