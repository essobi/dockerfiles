FROM python  
MAINTAINER Shubham Shukla  
  
RUN pip install twisted  
RUN mkdir load_balancer  
ADD . load_balancer/  
# No need to EXPOSE here if we are EXPOSING all ports using -P in docker run  
# command.  
# EXPOSE 8007 8008 8009  

