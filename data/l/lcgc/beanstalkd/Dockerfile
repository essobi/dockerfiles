FROM alpine:3.2  
MAINTAINER Eagle Liut <eagle@dantin.me>  
  
ENV version="1.10"  
RUN apk --update add --virtual build-dependencies \  
gcc \  
make \  
musl-dev \  
curl \  
&& curl -sL https://github.com/kr/beanstalkd/archive/v$version.tar.gz | tar
xvz -C /tmp \  
&& cd /tmp/beanstalkd-$version \  
&& sed -i "s|#include <sys/fcntl.h>|#include <fcntl.h>|g" sd-daemon.c \  
&& make \  
&& cp beanstalkd /usr/bin \  
&& apk del build-dependencies \  
&& rm -rf /tmp/* \  
&& rm -rf /var/cache/apk/*  
  
EXPOSE 11300  
CMD ["beanstalkd", "-p", "11300", "-u", "nobody"]  

