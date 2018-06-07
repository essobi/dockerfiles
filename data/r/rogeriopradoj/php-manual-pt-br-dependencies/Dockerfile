FROM alpine:latest  
  
MAINTAINER rogeriopradoj <rogeriopradoj@gmail.com>  
  
RUN apk add --no-cache php-cli && \  
apk add --no-cache php-pear && \  
apk add --no-cache php-xmlreader && \  
apk add --no-cache php-sqlite3 && \  
apk add --no-cache php-zlib && \  
apk add --no-cache php-json && \  
apk add --no-cache git && \  
apk add --no-cache subversion && \  
apk add --no-cache rsync && \  
rm -rf /var/cache/apk/* && \  
sed -ie 's/memory_limit\ =\ .*/memory_limit\ =\ -1/g' /etc/php/php.ini && \  
git clone http://git.php.net/repository/phd.git && \  
cd phd && \  
pear install package.xml package_generic.xml package_php.xml && \  
cd .. && \  
rm -rf phd  

