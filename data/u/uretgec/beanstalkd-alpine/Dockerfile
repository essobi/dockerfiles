FROM alpine:3.4  
MAINTAINER Tuna Aras <iletisim@uretgec.com>  
  
ENV VERSION_BEANSTALKD="1.10"  
RUN addgroup -S beanstalkd && adduser -S -G beanstalkd beanstalkd  
RUN apk add --no-cache 'su-exec>=0.2'  
  
RUN apk --update add --virtual build-dependencies \  
gcc \  
make \  
musl-dev \  
curl \  
&& curl -sL
https://github.com/kr/beanstalkd/archive/v$VERSION_BEANSTALKD.tar.gz | tar xvz
-C /tmp \  
&& cd /tmp/beanstalkd-$VERSION_BEANSTALKD \  
&& sed -i "s|#include <sys/fcntl.h>|#include <fcntl.h>|g" sd-daemon.c \  
&& make \  
&& cp beanstalkd /usr/bin \  
&& apk del build-dependencies \  
&& rm -rf /tmp/* \  
&& rm -rf /var/cache/apk/*  
  
RUN mkdir /data && chown beanstalkd:beanstalkd /data  
VOLUME ["/data"]  
EXPOSE 11300  
ENTRYPOINT ["beanstalkd", "-p", "11300", "-u", "beanstalkd"]  
CMD ["-b", "/data"]  

