FROM shurshun/alpine-moscow  
  
LABEL SERVICE_NAME="beanstalkd"  
  
ENV VERSION_BEANSTALKD="1.10"  
HEALTHCHECK CMD /bin/beanschk  
  
RUN addgroup -S beanstalkd && adduser -S -G beanstalkd beanstalkd  
  
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
  
RUN \  
BEANSCHK_VERSION=$(curl -s https://api.github.com/repos/shurshun/beanschk/tags
| jq -r ".[0] .name") \  
&& curl -fSlL
https://github.com/shurshun/beanschk/releases/download/${BEANSCHK_VERSION}/beanschk_${BEANSCHK_VERSION}_linux_amd64.tar.gz
| tar -C /bin -zx  
  
RUN mkdir /var/lib/beanstalkd && chown beanstalkd:beanstalkd
/var/lib/beanstalkd  
  
VOLUME ["/var/lib/beanstalkd"]  
  
EXPOSE 11300  
ENTRYPOINT ["beanstalkd", "-l", "0.0.0.0", "-p", "11300", "-u", "beanstalkd"]  
CMD ["-b", "/var/lib/beanstalkd", "-f", "5000"]  

