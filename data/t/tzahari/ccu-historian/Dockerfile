FROM nathonfowlie/centos-jre  
MAINTAINER Thomas Zahari <thomas.zahari@gmail.com>  
  
ADD ./install.sh /tmp/  
ADD ./start.sh /tmp/  
  
WORKDIR /tmp  
  
RUN bash -el /tmp/install.sh 2>/var/log/install_error.log  
  
ENV CONFIG_TYPE=CCU2  
  
EXPOSE 80 2011  
VOLUME ["/database","/opt/ccu-historian/config"]  
  
ENTRYPOINT ["/opt/ccu-historian/start.sh"]  

