FROM ubuntu:latest  
RUN groupmod -g 82 www-data \  
&& usermod -u 82 www-data  
RUN apt update \  
&& apt-get install -y libnghttp2-dev libpcre3-dev libexpat1-dev libssl-dev
zlib1g-dev wget build-essential libmysqlclient20 libcurl4-openssl-dev libcurl3
libxml2-dev libxml2 libexpat1 libnghttp2-14 \  
&& rm -rf /var/lib/apt/lists/*  
WORKDIR /usr/local/src  
ENV HTTPD_VERSION 2.4.29  
RUN wget http://apache.cp.if.ua/httpd/httpd-$HTTPD_VERSION.tar.gz \  
&& mkdir httpd \  
&& tar xfz httpd-2.4.29.tar.gz -C /usr/local/src/httpd --strip=1  
WORKDIR httpd  
RUN wget http://apache.cp.if.ua/apr/apr-1.6.3.tar.gz \  
&& mkdir srclib/apr \  
&& tar xfz apr-1.6.3.tar.gz -C srclib/apr --strip=1  
RUN wget http://apache.cp.if.ua/apr/apr-util-1.6.1.tar.gz \  
&& mkdir srclib/apr-util \  
&& tar xfz apr-util-1.6.1.tar.gz -C srclib/apr-util --strip=1  
RUN CFLAGS="-DDYNAMIC_MODULE_LIMIT=0"; export CFLAGS \  
&& ./configure --prefix=/usr/local/apache2 \  
--enable-speling=static \  
--enable-deflate=static \  
--enable-expires=static \  
--enable-headers=static \  
--enable-rewrite=static \  
--with-included-apr \  
--with-mpm=event \  
--enable-suexec=static \  
--with-suexec-docroot=/var/www \  
--enable-nonportable-atomics=yes \  
--with-pcre=static \  
--enable-authz-core=static \  
--enable-cache=static \  
--enable-cache-disk=static \  
--enable-cgid=static \  
--enable-http2=static \  
--enable-mime-magic=static \  
--enable-vhost-alias=static \  
--enable-unique-id=static \  
--enable-unixd=static \  
--enable-dir=static \  
--enable-log-sql=shared \  
--enable-log-sql-mysql=shared \  
--enable-log-sql-ssl=shared \  
--enable-filter=static \  
--enable-mime=static \  
--enable-actions=static \  
--enable-alias=static \  
--enable-proxy=static \  
--enable-proxy-fcgi=static \  
--enable-slotmem-shm=static \  
--enable-socache-shmcb=static \  
--enable-status=static \  
--enable-authz-host=static \  
--enable-setenvif=static \  
--enable-log-config=static \  
&& make \  
&& make install  
#RUN wget https://www.modsecurity.org/tarball/2.9.2/modsecurity-2.9.2.tar.gz \  
#&& tar xfz modsecurity-2.9.2.tar.gz  
#WORKDIR modsecurity-2.9.2  
#RUN ./configure --with-apxs=/usr/local/apache2/bin/apxs --with-
apr=/usr/local/src/httpd/srclib/apr --with-
apu=/usr/local/src/httpd/srclib/apr-util/ \  
#&& make \  
#&& make install \  
#&& cp /usr/local/modsecurity/lib/mod_security2.so /usr/local/apache2/modules/  
WORKDIR /usr/local/apache2/  
RUN rm -rf /usr/local/src/* \  
&& apt-get purge -y --auto-remove libnghttp2-dev libpcre3-dev libexpat1-dev
libssl-dev zlib1g-dev wget build-essential libcurl4-openssl-dev libxml2-dev  
#COPY mod_log_sql.so modules/  
#COPY mod_log_sql_mysql.so modules/  
#COPY mod_log_sql_ssl.so modules/  
CMD ["bin/apachectl","-DFOREGROUND"]  

