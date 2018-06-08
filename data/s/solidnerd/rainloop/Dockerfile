FROM alpine:3.4  
MAINTAINER Niclas Mietz niclas@mietz.io  
  
ENV RAINLOOP_VERSION 1.10.5.192  
ENV RAINLOOP_BUILD="/etc/rainloop" \  
RAINLOOP_HOME="/var/www/rainloop" \  
RAINLOOP_CLONE_URL="https://github.com/RainLoop/rainloop-webmail.git" \  
REQUIRED_PACKAGES="apache2 php5-apache2 php5-openssl php5-xml php5-json
php5-iconv php5-curl php5-pdo_mysql php5-pdo_pgsql php5-pdo_sqlite php5-dom
php5-zlib"  
RUN \  
apk add --no-cache $REQUIRED_PACKAGES && \  
mkdir -p /run/apache2 && \  
rm -fr /var/cache/apk/* && \  
rm -fr /usr/bin/php  
  
RUN echo "@commuedge https://nl.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories && \  
echo "@testing https://nl.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories && \  
apk add -U git nodejs findutils && \  
npm install gulp -g && \  
git clone -q -b v${RAINLOOP_VERSION} \--depth 1 ${RAINLOOP_CLONE_URL}
${RAINLOOP_BUILD} && \  
cd ${RAINLOOP_BUILD} && \  
npm install && \  
gulp rainloop:start && \  
mv build/dist/releases/webmail/${RAINLOOP_VERSION}/src ${RAINLOOP_HOME} && \  
npm uninstall -g gulp && \  
apk del --purge git nodejs && \  
rm -fr ${RAINLOOP_BUILD} /root/.npm /tmp/* /var/cache/apk/*  
  
ADD httpd.conf /etc/apache2/httpd.conf  
  
WORKDIR $RAINLOOP_HOME  
  
EXPOSE 80  
VOLUME /var/www/rainloop/data  
  
ADD docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  

