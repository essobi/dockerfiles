FROM resin/armv7hf-debian:stretch  
MAINTAINER Curtis Muntz <me@murt.is>  
RUN [ "cross-build-start" ]  
  
COPY install_prereqs.sh /opt/install_prereqs.sh  
RUN bash /opt/install_prereqs.sh  
  
RUN [ "cross-build-end" ]  

