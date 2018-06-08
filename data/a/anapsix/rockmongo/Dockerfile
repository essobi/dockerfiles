FROM alpine  
MAINTAINER Anastas Dancha <anapsix@random.io>  
RUN apk upgrade \--update && \  
apk add php-cli php-dev php-pear autoconf openssl-dev g++ make && \  
pear update-channels && \  
php /usr/share/pear/peclcmd.php install -f mongo && \  
echo "extension=mongo.so" >> /etc/php/php.ini && \  
apk del --purge php-dev php-pear autoconf openssl-dev g++ make  
ADD . /rockmongo  
WORKDIR /rockmongo  
EXPOSE 5000  
CMD ["php","-S","0.0.0.0:5000"]  
  
## NOTES  
# mount your config.php with "-v /path/to/config.php:/rockmongo/config.php"  
# this container supports alternative Auth DB,  
# i.e. if you are connecting to "test" and need to auth against "admin"  
# you may specify Auth DB in "More >>"  
# start it like so:  
# docker run -it --rm -p 5000:5000 -v
/path/to/config.php:/rockmongo/config.php anapsix/rockmongo  
# PECL script is broken in Alpine 3.2  
# running it without any arguments seems to work  

