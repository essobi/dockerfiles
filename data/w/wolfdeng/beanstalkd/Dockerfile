FROM wolfdeng/alpine:3.6  
MAINTAINER Tony Deng ( wolf.deng@gmail.com )  
  
## add Tini and Beanstalkd  
RUN apk add --update --no-cache tini beanstalkd && rm -rf /var/cache/apk/*  
  
ENTRYPOINT ["/sbin/tini","--"]  
  
## Expose the port  
EXPOSE 11300  
## Beanstalkd binlog setting  
RUN mkdir -p /mnt/beanstalkd/binlog  
RUN chown -R beanstalk /mnt/beanstalkd  
  
## Beanstalkd Run  
CMD
["beanstalkd","-p","11300","-u","beanstalk","-b","/mnt/beanstalkd/binlog","-V"]  

