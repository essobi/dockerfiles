FROM ubuntu:14.04  
MAINTAINER Daniel Foote <freefoote@dview.net>  
  
RUN apt-get update -q  
RUN apt-get -qy install beanstalkd=1.9-2ubuntu1  
RUN mkdir /binlog  
RUN chown beanstalkd.beanstalkd /binlog  
  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD start.sh /start.sh  
  
EXPOSE 11300  
VOLUME ["/binlog"]  
CMD ["/start.sh"]  

