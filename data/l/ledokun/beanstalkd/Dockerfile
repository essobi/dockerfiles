FROM schickling/beanstalkd  
  
MAINTAINER Rom Luengwattanapong <s1567783@ed.ac.uk>  
  
RUN mkdir -p /data  
  
VOLUME ["/data"]  
CMD ["beanstalkd", "-p", "11300", "-b", "/data"]  

