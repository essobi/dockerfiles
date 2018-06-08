FROM alpine  
ENV VERSION=1.3.1  
RUN apk add --no-cache bash curl mysql-client php7-imap php7-pdo_mysql
php7-dom php7-json php7-openssl php7-sockets php7-iconv php7-zip \  
&& curl --location
https://github.com/roundcube/roundcubemail/releases/download/${VERSION}/roundcubemail-${VERSION}-complete.tar.gz
| tar xzf - \  
&& mv roundcubemail* /www \  
&& curl --remote-name
http://svn.apache.org/repos/asf/httpd/httpd/trunk/docs/conf/mime.types \  
&& mkdir /config  
COPY config.php php.ini run.sh /  
CMD /run.sh  

