FROM tianon/ubuntu-core:14.04  
ADD build.sh /tmp/build.sh  
RUN /tmp/build.sh  
  
RUN mkdir -p /etc/confd  
ADD confd.toml /etc/confd/  
ADD conf.d /etc/confd/conf.d  
ADD templates /etc/confd/templates  

