FROM alpine:3.7  
RUN apk add --no-cache beanstalkd  
  
RUN mkdir /binlog && chown nobody /binlog  
VOLUME ["/binlog"]  
  
ENTRYPOINT ["beanstalkd"]  
CMD ["-b", "/binlog", "-u", "nobody"]  

