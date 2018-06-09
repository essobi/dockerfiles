FROM ubuntu  
  
MAINTAINER Youcef Medjellakh  
  
RUN apt-get update  
  
RUN apt-get install -y memcached  
  
EXPOSE 80  
RUN apt-get -y install nmap  
  
ENTRYPOINT ["nmap"]  
  

