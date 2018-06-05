FROM alpine:edge  
  
RUN apk update && apk add --no-cache beanstalkd  
  
EXPOSE 11300  
CMD ["/usr/bin/beanstalkd"]  

