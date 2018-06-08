FROM alpine  
MAINTAINER Allen Wang <ggtwlb0314@gmail.com">  
  
RUN apk update && apk add squid  
  
ADD conf /etc/squid  
  
CMD /usr/sbin/squid -N -YC -f /etc/squid/squid.conf  

