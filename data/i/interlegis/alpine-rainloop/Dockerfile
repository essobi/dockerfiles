FROM alpine:3.4  
MAINTAINER Niclas Mietz niclas@mietz.io  
  
ENV RAINLOOP_VERSION 1.11.0.203  
ENV RAINLOOP_BUILD="/etc/rainloop" \  
RAINLOOP_HOME="/var/www/rainloop" \  
REQUIRED_PACKAGES="apache2 php5-apache2 php5-openssl php5-xml php5-json
php5-iconv php5-curl php5-pdo_mysql php5-pdo_pgsql php5-pdo_sqlite php5-dom
php5-zlib php5-ldap unzip curl"  
RUN \  
apk update && \  
apk add --no-cache $REQUIRED_PACKAGES && \  
mkdir -p /run/apache2 && \  
rm -fr /var/cache/apk/* && \  
rm -fr /usr/bin/php  
  
RUN echo "@commuedge https://nl.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories && \  
echo "@testing https://nl.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories && \  
mkdir -p ${RAINLOOP_HOME} && \  
cd ${RAINLOOP_HOME} && \  
curl -L -O https://github.com/RainLoop/rainloop-
webmail/releases/download/v${RAINLOOP_VERSION}/rainloop-
community-${RAINLOOP_VERSION}.zip && \  
unzip *.zip && \  
rm -f *.zip && \  
find . -type d -exec chmod 755 {} \; && \  
find . -type f -exec chmod 644 {} \; && \  
chown -R apache: *  
  
  
ADD httpd.conf /etc/apache2/httpd.conf  
ADD php-maxsize.ini /etc/php5/conf.d/maxsize.ini  
  
WORKDIR $RAINLOOP_HOME  
  
EXPOSE 80  
VOLUME /var/www/rainloop/data  
  
ADD docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  

