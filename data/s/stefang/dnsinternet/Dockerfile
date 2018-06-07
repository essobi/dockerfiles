FROM debian:wheezy  
MAINTAINER Stefan Gotkowski  
RUN apt-get update && apt-get install -y bind9  
ADD scriptDNS.sh /script.sh  
RUN chmod +x /script.sh  
ADD zone /zone  
EXPOSE 53 53/udp  
ENTRYPOINT /script.sh  

