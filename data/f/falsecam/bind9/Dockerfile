FROM debian:wheezy  
RUN apt-get update  
RUN apt-get install -y bind9  
VOLUME /etc/bind  
EXPOSE 53 53/udp  
ENTRYPOINT ["/usr/sbin/named", "-g"]  

