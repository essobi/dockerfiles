FROM php:7.1.3-alpine  
  
MAINTAINER herloct <herloct@gmail.com>  
  
ENV COMPOSER_VERSION=1.4.1 \  
COMPOSER_HOME=/composer \  
PATH=$COMPOSER_HOME/vendor/bin:$PATH  
  
COPY install-composer.sh /usr/local/bin/install-composer.sh  
  
RUN apk update --no-cache \  
&& apk add --no-cache \  
curl \  
git \  
mercurial \  
openssh \  
openssl \  
subversion \  
  
&& mkdir -p $COMPOSER_HOME \  
&& ( \  
cd /tmp \  
&& install-composer.sh \  
&& rm /usr/local/bin/install-composer.sh \  
) \  
  
&& export COMPOSER_ALLOW_SUPERUSER=1 \  
&& composer global require -a --prefer-dist "hirak/prestissimo:^0.3" \  
&& export COMPOSER_ALLOW_SUPERUSER=0 \  
  
&& chmod -R 0777 $COMPOSER_HOME/cache \  
  
&& rm -rf /var/cache/apk/* /var/tmp/* /tmp/* $COMPOSER_HOME/cache/*  
  
VOLUME ["/project", "$COMPOSER_HOME/cache"]  
WORKDIR /project  
  
ENTRYPOINT ["composer"]  
CMD ["--version"]  

