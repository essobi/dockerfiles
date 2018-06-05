FROM alpine:3.4  
RUN apk add --no-cache --repository http://dl-
cdn.alpinelinux.org/alpine/edge/community/ beanstalkd && \  
addgroup -S beanstalkd && adduser -D -S -s /sbin/nologin -G beanstalkd
beanstalkd && \  
mkdir -p /var/beanstalkd/data && chown -R beanstalkd:beanstalkd
/var/beanstalkd && \  
/usr/bin/beanstalkd -v  
  
WORKDIR /var/beanstalkd  
VOLUME /var/beanstalkd/data  
  
EXPOSE 11300  
ENTRYPOINT ["beanstalkd"]  
CMD ["-p", "11300", "-u", "beanstalkd", "-b", "/var/beanstalkd/data", "-f",
"100"]  

