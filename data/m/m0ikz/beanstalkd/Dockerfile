FROM m0ikz/centos6  
  
MAINTAINER Nicolás de la Torre <ndelatorre@moikz.com.ar>  
  
RUN yum install beanstalkd -y && yum clean all -y  
  
EXPOSE 11300  
ENTRYPOINT ["usr/bin/beanstalkd"]  
CMD ["-u", "nobody"]  

