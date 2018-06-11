FROM debian:jessie  
  
RUN apt-get update && apt-get install -y squid3 python-pip && pip install
j2cli  
  
RUN apt-get install -y sudo  
  
COPY squid.conf.j2 /etc/squid3/squid.conf.j2  
  
EXPOSE 3128  
COPY start.sh /start.sh  
CMD exec /start.sh  

