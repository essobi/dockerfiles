FROM alpine:edge  
MAINTAINER Hearst Automation Team <atat@hearst.com>  
  
ENV DOKU_HOME /opt/dokuwiki  
  
RUN apk update  
  
# Setup and install base components  
RUN apk add \  
bash \  
wget \  
tar \  
gzip \  
curl \  
lighttpd  
  
# Install all needed php packages  
RUN apk add \  
php-common \  
php-zlib \  
php-openssl \  
php-iconv \  
php-json \  
php-gd \  
php-curl \  
php-xml \  
php-pgsql \  
php-imap \  
php-cgi \  
fcgi \  
php-pdo \  
php-pdo_pgsql \  
php-soap \  
php-xmlrpc \  
php-posix \  
php-mcrypt \  
php-gettext \  
php-ldap \  
php-ctype \  
php-dom \  
&& rm -rf /var/cache/apk/*  
  
RUN mkdir -p $DOKU_HOME  
  
WORKDIR $DOKU_HOME  
  
# Download dokuwiki  
RUN wget -O $DOKU_HOME/dokuwiki.tgz \  
"http://download.dokuwiki.org/src/dokuwiki/dokuwiki-stable.tgz"  
  
# Ignore internal folder name, just extract the good bits  
RUN tar -zxf dokuwiki.tgz --strip-components=1  
  
# Set ownership and access  
RUN chmod -R 755 $DOKU_HOME /var/log/lighttpd  
RUN chmod -R 777 $DOKU_HOME  
RUN chown -R lighttpd:lighttpd $DOKU_HOME /var/log/lighttpd /var/run/lighttpd  
  
# Run cgi fix  
RUN sed -i -e "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g" /etc/php/php.ini  
  
# Configure lighttpd  
ADD lighttpd.conf /etc/lighttpd/lighttpd.conf  
  
# Cleanup  
RUN rm dokuwiki.tgz  
  
EXPOSE 80  
VOLUME $DOKU_HOME/data  
VOLUME $DOKU_HOME/lib/plugins  
VOLUME $DOKU_HOME/conf  
VOLUME $DOKU_HOME/lib/tpl  
  
ENTRYPOINT ["lighttpd", "-D", "-f", "/etc/lighttpd/lighttpd.conf"]  

