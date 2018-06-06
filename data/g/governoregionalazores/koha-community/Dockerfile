FROM ubuntu:16.04  
ENV TERM xterm  
ENV SKIP_SET_KERNEL_PARAMETERS true  
  
RUN apt-get update && apt-get install -y apache2 \  
wget \  
libapache2-mpm-itk \  
vim \  
memcached  
  
RUN a2enmod rewrite  
RUN a2enmod cgi  
RUN a2enmod deflate  
RUN a2enmod headers proxy_http  
  
RUN cd /usr/sbin && sed -i 's@101@0@g' policy-rc.d  
  
RUN echo 'deb http://debian.koha-community.org/koha stable main' | tee
/etc/apt/sources.list.d/koha.list  
RUN wget -O- http://debian.koha-community.org/koha/gpg.asc | apt-key add -  
RUN apt-get update && apt-get install -y koha-common  
  
RUN cd /etc/koha && sed -i 's@INTRAPORT="80"@INTRAPORT="8080"@g' koha-
sites.conf \  
&& sed -i 's@DOMAIN=".myDNSname.org"@DOMAIN=""@g' koha-sites.conf  
  
RUN cd /etc/koha && sed -i 's@OPACPORT="80"@OPACPORT="8081"@g' koha-sites.conf  
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf  
  
RUN cd /etc/apache2 \  
&& echo "Listen 8080" >> ports.conf \  
&& echo "Listen 8081" >> ports.conf  
  
ADD koha-common.cnf /etc/mysql/  
ADD koha-create /usr/sbin/koha-create  
RUN cd /usr/sbin && chmod 755 koha-create  
RUN cd /etc/mysql && koha-create --request-db --marcflavor unimarc koha  
  
RUN koha-translate --install pt-PT  
RUN koha-create --populate-db --marcflavor unimarc koha  
ADD koha.conf /etc/apache2/sites-available/koha.conf  
RUN sed -i
"s@<memcached_servers></memcached_servers>@<memcached_servers>127.0.0.1:11211</memcached_servers>@g"
/etc/koha/sites/koha/koha-conf.xml  
RUN sed -i
"s@<memcached_namespace></memcached_namespace>@<memcached_namespace>koha</memcached_namespace>@g"
/etc/koha/sites/koha/koha-conf.xml  
RUN sed -i
"s@<enable_plugins>0</enable_plugins>@<enable_plugins>1</enable_plugins>@g"
/etc/koha/sites/koha/koha-conf.xml  
  
RUN chown -R koha-koha:koha-koha /etc/koha/sites/koha/  
RUN chown -R koha-koha:koha-koha /var/lib/koha/koha/  
  
ENV PERL5LIB /usr/share/koha/lib/  
ENV KOHA_CONF /etc/koha/sites/koha/koha-conf.xml  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_PID_FILE /var/run/apache2.pid  
ENV APACHE_RUN_DIR /var/run/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_USER_UID www-data  
  
COPY start.sh /start.sh  
CMD ["/bin/bash", "/start.sh"]  
  

