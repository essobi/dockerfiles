FROM alpine:3.6  
  
ENV UID=911 \  
GID=911  
  
# Install required packages  
RUN apk add \--no-cache --update \  
bash \  
coreutils \  
ca-certificates \  
openssl \  
shadow \  
pcre \  
apache2 \  
php7 \  
php7-apache2 \  
php7-common \  
php7-openssl \  
php7-json \  
php7-phar \  
php7-curl \  
php7-zlib \  
php7-pdo \  
php7-dom \  
php7-simplexml \  
php7-xmlreader \  
php7-xmlwriter \  
php7-mbstring \  
php7-ctype \  
php7-iconv \  
  
&& update-ca-certificates \  
&& sed -i "s/#LoadModule\ rewrite_module/LoadModule\ rewrite_module/"
/etc/apache2/httpd.conf  
  
COPY root /  
  
# Create directories  
RUN mkdir -p /locks /webdav /var/log /run/apache2 \  
  
# Create user  
&& groupmod -g 1000 users \  
&& useradd -u ${UID} -U -s /bin/false -d /webdav webdav \  
&& usermod -G users webdav \  
  
# Setting permissions  
&& chown webdav:webdav /locks /webdav \  
&& chmod a+rwx /locks /webdav \  
  
# Install composer and download deps  
&& chmod a+rwx /sabre/build.sh /sabre/run.sh \  
&& /sabre/build.sh  
  
VOLUME ["/webdav", "/locks"]  
  
EXPOSE 80  
  
CMD /sabre/run.sh  

