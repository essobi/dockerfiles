FROM alpine  
MAINTAINER Nektria "it@nektria.com"  
RUN apk --update add beanstalkd  
  
RUN rm -rf /var/cache/apk/*  
  
EXPOSE 11300  
CMD ["beanstalkd", "-p", "11300"]  

