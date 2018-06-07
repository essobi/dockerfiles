FROM alpine:latest  
  
RUN apk add --no-cache beanstalkd  
  
RUN mkdir /data  
  
EXPOSE 11300  
ENTRYPOINT ["beanstalkd", "-b", "/data", "-p", "11300"]  

