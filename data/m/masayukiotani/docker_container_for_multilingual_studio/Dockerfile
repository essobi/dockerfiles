# install PHP  
FROM php:7.0.2-apache  
  
# get apt-get package set  
RUN apt-get update  
  
# install required packages  
RUN apt-get install -y apt-utils  
RUN apt-get install -y git  
RUN apt-get install -y vim  
RUN apt-get install -y locales  
RUN apt-get install -y locate  
RUN updatedb  
  
RUN dpkg-reconfigure locales && \  
locale-gen C.UTF-8 && \  
/usr/sbin/update-locale LANG=C.UTF-8  
  
ENV LC_ALL C.UTF-8  
# install apache and php related file  
RUN apt-get install -y aptitude  
RUN aptitude install libxml2-dev  
RUN pear install soap-0.13.0  
RUN docker-php-ext-install soap  
RUN docker-php-ext-install mbstring  
  
CMD /usr/sbin/apache2ctl -D FOREGROUND  
  
# install MultilingualStudio  
RUN git clone https://github.com/langrid/langrid-php-library.git  
RUN git clone https://github.com/jpfuentes2/php-activerecord.git  
RUN rm -rf langrid-php-library/lib/php-activerecord  
RUN mv -f php-activerecord langrid-php-library/lib/php-activerecord  
RUN rm -rf php-activerecord  

