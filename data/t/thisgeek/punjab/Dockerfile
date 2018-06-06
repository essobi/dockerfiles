# Punjab  
FROM ubuntu:precise  
MAINTAINER Matthew Seddon <dark@midnightreign.org>  
  
RUN apt-get update  
RUN apt-get -y install python-twisted wget unzip dnsmasq-base  
  
# dnsmasq  
RUN echo 'listen-address=127.0.0.1' >> /etc/dnsmasq.conf  
RUN echo 'resolv-file=/etc/resolv.dnsmasq.conf' >> /etc/dnsmasq.conf  
RUN echo 'nameserver 8.8.8.8' >> /etc/resolv.dnsmasq.conf  
RUN echo 'nameserver 8.8.4.4' >> /etc/resolv.dnsmasq.conf  
  
# punjab  
RUN cat /proc/mounts > /etc/mtab  
RUN mkdir -p /src \  
&& cd /src \  
&& wget --no-check-certificate
https://github.com/twonds/punjab/archive/master.zip -O punjab-src.zip \  
&& unzip punjab-src.zip \  
&& cd punjab-master \  
&& python setup.py install \  
&& cd /  
  
ADD ./start.sh /  
RUN chmod a+x /start.sh  
  
EXPOSE 5280  
CMD ["/start.sh"]  
  

