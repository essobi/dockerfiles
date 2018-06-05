FROM alpine:3.4  
MAINTAINER Nikola Petkanski <nikola@petkanski.com>  
  
RUN adduser -u 1000 -D -g '' www-data  
  
RUN echo "http://dl-4.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories && \  
apk --update add beanstalkd  
  
EXPOSE 11300  
CMD ["beanstalkd", "-p", "11300"]  

