FROM alpine:3.5  
MAINTAINER Adam Kusmierz <adam@kusmierz.be>  
  
## Add Tini and Beanstalkd  
RUN apk add --update --no-cache tini beanstalkd && rm -fr /var/cache/apk/*  
ENTRYPOINT ["/sbin/tini", "--"]  
  
## Expose the port  
EXPOSE 11300  
CMD ["beanstalkd", "-p", "11300", "-u", "nobody"]  

