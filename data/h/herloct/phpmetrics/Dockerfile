FROM php:7.1.1-alpine  
  
MAINTAINER herloct <herloct@gmail.com>  
  
ENV PHP_METRICS_VERSION=2.0.0  
RUN curl -L
https://github.com/phpmetrics/PhpMetrics/releases/download/v$PHP_METRICS_VERSION/phpmetrics.phar
> /usr/local/bin/phpmetrics \  
&& chmod +x /usr/local/bin/phpmetrics \  
  
&& rm -rf /var/cache/apk/* /var/tmp/* /tmp/*  
  
VOLUME ["/project"]  
WORKDIR /project  
  
ENTRYPOINT ["phpmetrics"]  
CMD ["--version"]  

