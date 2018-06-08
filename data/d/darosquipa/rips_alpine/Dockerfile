FROM alpine:3.6  
LABEL description="Simple Image RIPS for security apps"  
LABEL version="1.0"  
LABEL maintainer="darosquipa@dtransforma.com"  
  
ENV VERSION_RIPS 0.55  
RUN apk --no-cache --update add bash tzdata xz php5-apache2 curl php5-cli
php5-json php5-phar php5-openssl && \  
rm -f /var/cache/apk/* && \  
curl -sS https://getcomposer.org/installer | php5 -- --install-
dir=/usr/local/bin --filename=composer && \  
mkdir /apps && chown -R apache:apache /apps && \  
sed -i 's#^DocumentRoot ".*#DocumentRoot "/apps"#g' /etc/apache2/httpd.conf &&
\  
sed -i 's#AllowOverride none#AllowOverride All#' /etc/apache2/httpd.conf && \  
curl "http://sourceforge.net/projects/rips-
scanner/files/rips-$VERSION_RIPS.zip/download" -L -o
/tmp/rips-$VERSION_RIPS.zip && \  
unzip /tmp/rips-$VERSION_RIPS.zip -d /apps && \  
rm /tmp/rips-$VERSION_RIPS.zip && \  
mv /apps/rips-$VERSION_RIPS/* /apps/ && \  
mkdir /work && \  
echo "Success"  
  
EXPOSE 80  
WORKDIR /apps  
  
ENTRYPOINT ["tail -F /var/log/apache2/*log", "httpd -D FOREGROUND"]  

