FROM jpetazzo/dind  
MAINTAINER Bernd Fischer <bfischer@mindapproach.de>  
  
COPY ./mapp-wrapdocker /usr/local/bin/mapp-wrapdocker  
RUN chmod +x /usr/local/bin/mapp-wrapdocker  
  
RUN mkdir /root/tls && chmod 700 /root/tls  
# COPY ./tls/ /root/tls/  
# RUN chmod 600 /root/tls/*  

