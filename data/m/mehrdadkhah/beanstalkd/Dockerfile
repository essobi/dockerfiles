FROM debian  
  
MAINTAINER Mehrdad Dadkhah <mehrdad@dadkhah.me>  
  
RUN apt-get update && \  
apt-get install -y vim && \  
apt-get install -y beanstalkd  
  
EXPOSE 11300  
CMD beanstalkd -p 11300 -z 524280  

