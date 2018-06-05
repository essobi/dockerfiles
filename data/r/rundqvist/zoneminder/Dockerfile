FROM alpine:3.7  
LABEL maintainer="mattias.rundqvist@icloud.com"  
  
VOLUME [ "/data", "/images", "/events" ]  
  
WORKDIR /app  
  
RUN apk add --update --no-cache \  
php7 php7-fpm php7-pdo php7-pdo_mysql php7-session php7-sockets php7-ctype
php7-cgi php7-soap php7-apcu php7-json \  
perl-data-uuid perl-data-dump perl-io-socket-ssl perl-xml-xpath \  
tzdata shadow lighttpd supervisor mariadb zoneminder  
  
RUN apk add --no-cache --virtual .build-deps make gcc musl-dev perl-dev expat-
dev php7-dev php7-pear \  
&& cpan -f install Class::Std::Fast \  
&& cpan -f install SOAP::WSDL \  
&& cpan -f install IO::Socket::Multicast \  
&& echo "n" | pecl install apcu_bc \  
&& apk del .build-deps \  
&& mkdir -p /home/buildozer/aports/community/zoneminder/src/ \  
&& wget
https://github.com/FriendsOfCake/crud/archive/c3976f1478c681b0bbc132ec3a3e82c3984eeed5.zip
\  
&& unzip c3976f1478c681b0bbc132ec3a3e82c3984eeed5.zip \  
&& mv crud-c3976f1478c681b0bbc132ec3a3e82c3984eeed5
/home/buildozer/aports/community/zoneminder/src/ \  
&& rm -f c3976f1478c681b0bbc132ec3a3e82c3984eeed5.zip \  
&& mkdir -p /run/mysqld \  
&& mkdir -p /var/lib/zoneminder/temp \  
&& mkdir -p /var/www/localhost/htdocs/zm \  
&& mkdir -p /var/lib/zoneminder/templogs \  
&& touch /var/log/zonemindererror.log \  
&& ln -s /images /var/www/localhost/htdocs/zm/images \  
&& ln -s /events /var/www/localhost/htdocs/zm/events \  
&& sed -i 's/\\(ZM_WEB_\\(USER\|GROUP\\)\\)=.*/\1=lighttpd/g' /etc/zm.conf \  
&& rm -rf /root/.cpan  
  
RUN touch /var/log/mysql.log  
  
COPY root /  
  
ENV TZ="" \  
UID="" \  
GID="" \  
OPTIMIZE=""  
EXPOSE 80  
HEALTHCHECK \--interval=60s --timeout=5s --start-period=30s \  
CMD /bin/sh /app/healthcheck.sh  
  
ENTRYPOINT [ "/app/entrypoint.sh" ]  

