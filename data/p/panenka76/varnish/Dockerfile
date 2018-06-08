FROM debian:jessie  
  
COPY varnish-cache.org.GPG /opt/varnish-cache.org.GPG  
ENV VARNISH_VERSION=4.1.6-1~jessie  
  
RUN apt-key add /opt/varnish-cache.org.GPG  
RUN echo "deb http://repo.varnish-cache.org/debian/ jessie varnish-4.1"\  
>> /etc/apt/sources.list.d/varnish-cache.list  
  
RUN apt-get update  
RUN apt-get install -y varnish=$VARNISH_VERSION  
  
COPY start.sh /opt/start.sh  
  
ENV VARNISH_PORT 80  
ENV VARNISH_MEMORY 100m  
  
CMD [ "/opt/start.sh" ]  

