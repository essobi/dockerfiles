FROM ubuntu:17.10  
MAINTAINER leenchan  
  
RUN apt-get update && apt-get install -y wget curl  
  
RUN wget -O /usr/bin/vps https://github.com/leenchan/vps/raw/master/vps.sh &&
chmod +x /usr/bin/vps && /usr/bin/vps docker  
  
ADD run.sh /run.sh  
RUN chmod +x /run.sh  
  
EXPOSE 22 80 443 5901 8443  
CMD ["/run.sh"]  

