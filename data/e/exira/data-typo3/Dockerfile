FROM exira/base:latest  
  
MAINTAINER exira.com <info@exira.com>  
  
ENV TYPO3_VERSION=7.6.4 \  
TYPO3_SHA1=d942dc969ec92387ed3b13a5c336f634  
  
RUN apk update && \  
apk upgrade && \  
apk add \--update \--no-cache wget && \  
  
# download unpack TYPO3  
mkdir /tmp/wp/ && \  
cd /tmp/wp/ && \  
wget
http://prdownloads.sourceforge.net/typo3/typo3_src-${TYPO3_VERSION}.tar.gz
\--no-check-certificate -O /tmp/typo3.tar.gz && \  
#echo "${TYPO3_SHA1} /tmp/typo3.tar.gz" | sha1sum -c - && \  
mkdir -p /var/www/public_html/ && \  
tar xfz /tmp/typo3.tar.gz -C /var/www/public_html && \  
cd /var/www/public_html/ && \  
ln -s typo3_src-${TYPO3_VERSION} typo3_src && \  
ln -s typo3_src/typo3 typo3 && \  
ln -s typo3_src/index.php index.php && \  
rm -f /tmp/typo3.tar.gz && \  
  
# add www-data user  
mkdir -p /home/www-data && \  
addgroup -g 433 -S www-data && \  
adduser -u 431 -S -D -G www-data -h /home/www-data -s /sbin/nologin www-data
&& \  
chown -R www-data:www-data /home/www-data && \  
  
# cleanup  
apk del wget && \  
rm -rf /var/cache/apk/*  
  
ADD root /  
  
RUN chown -R www-data:www-data /var/www  
  
WORKDIR /var/www/  
  
VOLUME /var/www/  

