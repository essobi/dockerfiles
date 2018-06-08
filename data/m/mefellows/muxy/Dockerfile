FROM debian:latest  
MAINTAINER Matt Fellows <m@onegeek.com.au>  
  
RUN apt-get update && apt-get install -y wget unzip iptables iproute net-tools
sudo  
RUN mkdir -p /opt/muxy/bin  
  
WORKDIR /opt/muxy  
  
RUN wget
https://github.com/mefellows/muxy/releases/download/v0.0.5/linux_amd64.zip -O
muxy.zip  
RUN unzip muxy.zip  
RUN mv muxy /opt/muxy/bin/  
RUN rm *.zip  
  
ENV PATH
/opt/muxy/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  
  
VOLUME ["/opt/muxy/conf"]  
  
CMD ["muxy", "proxy", "--config", "/opt/muxy/conf/config.yml"]  

