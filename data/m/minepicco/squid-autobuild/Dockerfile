from centos:7  
RUN yum -y update && yum -y install squid && yum -y install wget && wget
https://raw.githubusercontent.com/minepicco/dockerfiles/master/squid/squid.conf  
# COPY squid.conf /etc/squid/squid.conf  
RUN chmod +x squid.conf  
RUN mv -f squid.conf /etc/squid/squid.conf  
ENTRYPOINT ["sh", "-c", "/etc/squid/squid start", "BACKGROUND"]  
  
EXPOSE 3128  

