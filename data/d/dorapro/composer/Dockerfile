FROM dorapro/php:7.0-alpine  
  
RUN set -x \  
&& mkdir -p /composer \  
&& mkdir -p /app \  
&& apk add --update --no-cache openssh-client git  
  
ENV COMPOSER_HOME /composer  
ENV PATH /composer/vendor/bin:$PATH  
ENV COMPOSER_ALLOW_SUPERUSER 1  
ENV COMPOSER_VERSION 1.2.0  
RUN curl -fsSL https://getcomposer.org/installer | php --
--version=${COMPOSER_VERSION} \--install-dir=/usr/local/bin
--filename=composer \  
&& composer global require hirak/prestissimo \  
&& composer global clear-cache  
  
VOLUME ["/app"]  
WORKDIR /app  
  
CMD ["--version"]  
ENTRYPOINT ["composer"]  

