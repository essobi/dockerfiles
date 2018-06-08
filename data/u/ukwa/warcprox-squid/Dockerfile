FROM centos:6.7  
RUN yum install -y squid  
  
COPY squid.conf /etc/squid/squid.conf  
  
EXPOSE 3128  
CMD squid -N  
  

