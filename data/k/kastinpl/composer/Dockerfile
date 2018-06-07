FROM php:cli  
  
# install and cleanup  
RUN apt-get update && apt-get -y install sudo zip git && \  
apt-get -y clean && apt-get -y purge && rm -rf /var/lib/apt/lists/*  
  
# install composer  
RUN php -r "readfile('https://getcomposer.org/installer');" > composer-
setup.php && \  
php composer-setup.php --filename=composer --install-dir=/bin && \  
rm -f composer-setup.php  
  
# create local user to map in as UID of /opt  
RUN adduser --disabled-password --home /home/php php  
  
# storing composer cache locally instead of docker  
VOLUME /home/php  
  
WORKDIR /opt  
  
# run php user as local  
COPY ./entrypoint.sh /  
ENTRYPOINT ["/entrypoint.sh"]

