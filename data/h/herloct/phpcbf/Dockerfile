FROM php:7.1.1-alpine  
  
MAINTAINER herloct <herloct@gmail.com>  
  
ENV PHPCBF_VERSION=2.8.1  
RUN curl -L
https://github.com/squizlabs/PHP_CodeSniffer/releases/download/$PHPCBF_VERSION/phpcbf.phar
> /usr/local/bin/phpcbf \  
&& chmod +x /usr/local/bin/phpcbf \  
  
&& rm -rf /var/cache/apk/* /var/tmp/* /tmp/*  
  
VOLUME ["/project"]  
WORKDIR /project  
  
ENTRYPOINT ["phpcbf"]  
CMD ["--version"]  

