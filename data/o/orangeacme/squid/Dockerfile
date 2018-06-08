FROM ubuntu:14.04  
MAINTAINER acme@astray.com  
  
RUN apt-get update && apt-get clean  
RUN apt-get install -y squid3 && apt-get clean  
ADD squid.conf /etc/squid3/squid.conf  
RUN mkdir /var/cache/squid  
RUN chown proxy:proxy /var/cache/squid  
RUN /usr/sbin/squid3 -N -z -F  
  
EXPOSE 3128  
CMD /usr/sbin/squid3 -N -d 0  

